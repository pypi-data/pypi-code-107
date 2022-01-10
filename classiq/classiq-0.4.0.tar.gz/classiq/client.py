import logging
import platform
import ssl
import urllib.parse
from typing import Any, Dict, Optional, Tuple, Union

import httpx
import pydantic
import websockets.client
from semver import VersionInfo

from classiq_interface import __version__ as classiq_interface_version
from classiq_interface.server import authentication
from classiq_interface.server.routes import ROUTE_PREFIX

from classiq import config
from classiq._version import VERSION as CLASSIQ_VERSION
from classiq.authentication import token_manager
from classiq.exceptions import ClassiqAPIError, ClassiqExpiredTokenError

_PROCESSED_VERSION = Union[VersionInfo, str]
_PROCESSED_VERSIONS = Tuple[_PROCESSED_VERSION, _PROCESSED_VERSION]


_VERSION_UPDATE_SUGGESTION = (
    'Run "pip install -U <PACKAGE>==<REQUIRED VERSION>" to resolve the conflict.'
)

_logger = logging.getLogger(__name__)


class HostVersions(pydantic.BaseModel):
    classiq_interface: pydantic.StrictStr = pydantic.Field()


class Client:
    _FRONTEND_VARIANT: str = "classiq-sdk"
    _UNKNOWN_VERSION = "0.0.0"

    def __init__(self, conf: config.Configuration):
        self._config = conf
        self._token_manager = token_manager.TokenManager()
        self._ssl_context = ssl.create_default_context()
        self._HTTP_TIMEOUT_SECONDS = (
            3600  # Needs to be synced with load-balancer timeout
        )

    @classmethod
    def _get_user_agent_header(cls) -> Dict[str, str]:
        return {
            "User-Agent": f"python/{platform.python_version()} ({platform.platform()}) {cls._FRONTEND_VARIANT}/{CLASSIQ_VERSION}"
        }

    @staticmethod
    def _handle_response(response: httpx.Response) -> Union[Dict, str]:
        if response.is_error:
            expired = (
                response.status_code == httpx.codes.UNAUTHORIZED
                and response.json()["detail"] == authentication.EXPIRED_TOKEN_ERROR
            )

            if expired:
                raise ClassiqExpiredTokenError("Expired token.")

            try:
                message = (
                    f"Call to API failed with code {response.status_code}: "
                    f"{response.json()['detail']}"
                )
            except BaseException:
                message = "Call to API failed"
            raise ClassiqAPIError(message)

        return response.json()

    def _make_client_args(self) -> Dict[str, Any]:
        return {
            "base_url": self._config.host,
            "timeout": self._HTTP_TIMEOUT_SECONDS,
            "headers": {
                **self._get_authorization_header(),
                **self._get_user_agent_header(),
            },
        }

    async def call_api(
        self, http_method: str, url: str, body: Optional[Dict] = None
    ) -> Union[Dict, str]:
        async with httpx.AsyncClient(**self._make_client_args()) as async_client:
            response = await async_client.request(
                method=http_method, url=url, json=body
            )
            return self._handle_response(response)

    def sync_call_api(
        self, http_method: str, url: str, body: Optional[Dict] = None
    ) -> Union[Dict, str]:
        with httpx.Client(**self._make_client_args()) as sync_client:
            response = sync_client.request(method=http_method, url=url, json=body)
            return self._handle_response(response)

    def _get_authorization_header(self) -> Dict[str, str]:
        access_token = self._token_manager.get_access_token()
        if access_token is None:
            return dict()
        return {"Authorization": f"Bearer {access_token}"}

    def _get_authorization_query_string(self) -> str:
        access_token = self._token_manager.get_access_token()
        if access_token is None:
            return ""
        return urllib.parse.urlencode({"token": access_token})

    async def update_expired_access_token(self) -> None:
        await self._token_manager.update_expired_access_token()

    def establish_websocket_connection(
        self, path: str, **kwargs
    ) -> websockets.client.connect:
        _MAX_PAYLOAD_SIZE = 2 ** 23  # = 8MiB ~= 8MB
        max_size = kwargs.get("max_size", _MAX_PAYLOAD_SIZE)
        ping_interval = kwargs.get("ping_interval", None)
        url = urllib.parse.urlsplit(self._config.ws_uri)
        url = url._replace(path=path, query=self._get_authorization_query_string())

        return websockets.client.connect(
            uri=url.geturl(),
            ssl=self._ssl_context if self._config.ws_uri.scheme == "wss" else None,
            max_size=max_size,
            ping_interval=ping_interval,
            extra_headers=self._get_user_agent_header(),
        )

    def get_backend_uri(self) -> str:
        return self._config.host

    def _get_host_version(self) -> str:
        host = HostVersions.parse_obj(
            self.sync_call_api("get", f"{ROUTE_PREFIX}/versions")
        )
        return host.classiq_interface

    @classmethod
    def _check_matching_versions(
        cls, lhs_version: str, rhs_version: str, normalize: bool = True
    ) -> bool:
        processed_versions: _PROCESSED_VERSIONS
        if normalize:
            # VersionInfo comparison is compatible with strings but it excludes any build info
            processed_versions = VersionInfo.parse(lhs_version), VersionInfo.parse(
                rhs_version
            )
        else:
            processed_versions = lhs_version, rhs_version
        if cls._UNKNOWN_VERSION in processed_versions:
            # In case one of those versions is unknown, they are considered equal
            _logger.debug(
                "Either {} or {} is an unknown version. Assuming both versions are equal.",
                lhs_version,
                rhs_version,
            )
            return True
        return processed_versions[0] == processed_versions[1]

    def check_host(self) -> None:
        # This function is NOT async (despite the fact that it can be) because it's called from a non-async context.
        # If this happens when we already run in an event loop (e.g. inside a call to asyncio.run), we can't go in to
        # an async context again.
        # Since this function should be called ONCE in each session, we can handle the "cost" of blocking the
        # event loop.
        if not self._check_matching_versions(
            classiq_interface_version, CLASSIQ_VERSION, normalize=False
        ):
            # When raising an exception, use the original strings
            raise ClassiqAPIError(
                f"Classiq API version mismatch: 'classiq' version is {CLASSIQ_VERSION}, "
                f"'classiq-interface' version is {classiq_interface_version}. {_VERSION_UPDATE_SUGGESTION}"
            )

        try:
            raw_host_version = self._get_host_version()
        except httpx.ConnectError:
            _logger.warning(
                "Version check failed - host unavailable.",
            )
        else:
            if not self._check_matching_versions(
                raw_host_version, classiq_interface_version
            ):
                raise ClassiqAPIError(
                    f"Classiq API version mismatch: 'classiq-interface' version is "
                    f"{classiq_interface_version}, backend version is {raw_host_version}. {_VERSION_UPDATE_SUGGESTION}"
                )

    async def authenticate(self, overwrite: bool) -> None:
        await self._token_manager.manual_authentication(overwrite=overwrite)


DEFAULT_CLIENT: Optional[Client] = None


def client() -> Client:
    global DEFAULT_CLIENT
    if DEFAULT_CLIENT is None:
        # This call initializes DEFAULT_CLIENT
        configure(config.init())
    assert DEFAULT_CLIENT is not None
    return DEFAULT_CLIENT


def configure(conf: config.Configuration) -> None:
    global DEFAULT_CLIENT
    assert DEFAULT_CLIENT is None, "Can not configure client after first usage."

    DEFAULT_CLIENT = Client(conf=conf)
    if conf.should_check_host:
        DEFAULT_CLIENT.check_host()
