import argparse
import sys
from racetrack_client.client.delete import delete_fatman

import yaml
import urllib3

from racetrack_client import __version__
from racetrack_client.client.deploy import send_deploy_request, DeploymentError
from racetrack_client.client.logs import show_runtime_logs, show_build_logs
from racetrack_client.client_config.auth import set_user_auth, AuthError
from racetrack_client.client_config.client_config import ClientConfig
from racetrack_client.client_config.io import load_client_config, save_client_config
from racetrack_client.client_config.update import set_credentials, set_config_setting, set_config_url_alias
from racetrack_client.log.exception import log_exception
from racetrack_client.log.logs import configure_logs
from racetrack_client.log.logs import get_logger
from racetrack_client.manifest.validate import load_validated_manifest

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description='CLI client tool for deploying workloads to Racetrack')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='enable verbose mode')
    subparsers = parser.add_subparsers()

    def _print_help(_: argparse.Namespace):
        parser.print_help(sys.stderr)

    parser.set_defaults(func=_print_help)

    # racetrack deploy
    parser_deploy = subparsers.add_parser(
        'deploy', help='Send request deploying a Fatman to the Racetrack cluster')
    parser_deploy.add_argument('workdir', default='.', nargs='?', help='directory with fatman.yaml manifest')
    parser_deploy.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_deploy.add_argument('--force', action='store_true', help='overwrite existing fatman')
    parser_deploy.set_defaults(func=_deploy)

    # racetrack validate
    parser_validate = subparsers.add_parser('validate', help='Validate Fatman manifest file')
    parser_validate.add_argument('path', default='.', nargs='?',
                                 help='path to a Fatman manifest file or to a directory with it')
    parser_validate.set_defaults(func=_validate)

    # racetrack logs
    parser_logs = subparsers.add_parser('logs', help='Show logs from fatman output')
    parser_logs.add_argument('workdir', default='.', nargs='?', help='directory with fatman.yaml manifest')
    parser_logs.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_logs.add_argument('--tail', default=20, nargs='?', type=int, help='number of recent lines to show')
    parser_logs.add_argument('--follow', '-f', action='store_true', help='follow logs output stream')
    parser_logs.set_defaults(func=_logs)

    # racetrack build-logs
    parser_build_logs = subparsers.add_parser('build-logs', help='Show build logs from fatman image building')
    parser_build_logs.add_argument('workdir', default='.', nargs='?', help='directory with fatman.yaml manifest')
    parser_build_logs.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_build_logs.add_argument('--tail', default=0, nargs='?', type=int,
                                   help='number of recent lines to show, all logs by default')
    parser_build_logs.set_defaults(func=_build_logs)

    # racetrack delete
    parser_delete = subparsers.add_parser('delete', help='Delete fatman instance')
    parser_delete.add_argument('workdir', default='.', nargs='?', help='directory with fatman.yaml manifest')
    parser_delete.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_delete.add_argument('--version', nargs='?', type=str,
                               help='fatman version to delete')
    parser_delete.set_defaults(func=_delete_fatman)

    # racetrack version
    parser_version = subparsers.add_parser('version', help='Show the version information')
    parser_version.set_defaults(func=_version)

    # racetrack config
    parser_config = subparsers.add_parser('config', help='Set local options for a Racetrack client')
    subparsers_config = parser_config.add_subparsers()

    # racetrack config show
    parser_config_show = subparsers_config.add_parser('show', help='Show racetrack config values')
    parser_config_show.set_defaults(func=_show_config)

    # racetrack config racetrack_url
    parser_config_racetrack_url = subparsers_config.add_parser(
        'racetrack_url', help='Set default Racetrack URL address')
    parser_config_racetrack_url.add_argument('setting_value', help='setting value')
    parser_config_racetrack_url.set_defaults(func=_set_config_racetrack_url)

    # racetrack config credentials
    parser_config_credentials = subparsers_config.add_parser(
        'credentials', help='Manage credentials for git repository access')
    subparsers_config_credentials = parser_config_credentials.add_subparsers()

    # racetrack config credentials set
    parser_config_credentials_set = subparsers_config_credentials.add_parser(
        'set', help='Set credentials for reading git repository')
    parser_config_credentials_set.add_argument('repo_url', help='git remote URL')
    parser_config_credentials_set.add_argument('username', help='username for git authentication')
    parser_config_credentials_set.add_argument('token_password', help='password or token for git authentication')
    parser_config_credentials_set.set_defaults(func=_set_config_credentials)

    # racetrack config alias
    parser_config_alias = subparsers_config.add_parser('alias', help='Manage aliases for Racetrack server URLs')
    subparsers_config_alias = parser_config_alias.add_subparsers()

    # racetrack config alias set
    parser_config_alias_set = subparsers_config_alias.add_parser(
        'set', help='Set up an alias for Racetrack server URL')
    parser_config_alias_set.add_argument('alias', help='short name for an environment')
    parser_config_alias_set.add_argument('racetrack_url', help='Racetrack server URL address')
    parser_config_alias_set.set_defaults(func=_set_config_url_alias)

    # racetrack login
    parser_login = subparsers.add_parser('login', help='Save user token for Racetrack server')
    parser_login.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_login.add_argument('user_token', default='', nargs='?', help='User token from RT user profile')
    parser_login.set_defaults(func=_login)

    # racetrack logout
    parser_logout = subparsers.add_parser('logout', help='Remove user token for Racetrack server')
    parser_logout.add_argument('racetrack_url', default='', nargs='?', help='URL to Racetrack server or alias name')
    parser_logout.set_defaults(func=_logout)

    args: argparse.Namespace = parser.parse_args()

    try:
        configure_logs(verbosity=args.verbose)
        args.func(args)
    except (DeploymentError, AuthError) as e:
        logger.error(str(e))  # no need for client's stacktrace in case of well known errors
    except Exception as e:
        log_exception(e)


def _deploy(args: argparse.Namespace):
    send_deploy_request(args.workdir, lifecycle_url=args.racetrack_url, force=args.force)


def _validate(args: argparse.Namespace):
    load_validated_manifest(args.path)


def _set_config_credentials(args: argparse.Namespace):
    set_credentials(args.repo_url, args.username, args.token_password)


def _set_config_racetrack_url(args: argparse.Namespace):
    set_config_setting('racetrack_url', args.setting_value)


def _set_config_url_alias(args: argparse.Namespace):
    set_config_url_alias(args.alias, args.racetrack_url)


def _logs(args: argparse.Namespace):
    show_runtime_logs(args.workdir, args.racetrack_url, args.tail, args.follow)


def _build_logs(args: argparse.Namespace):
    show_build_logs(args.workdir, args.racetrack_url, args.tail)


def _delete_fatman(args: argparse.Namespace):
    delete_fatman(args.workdir, args.racetrack_url, args.version)


def _show_config(args: argparse.Namespace):
    client_config = load_client_config()
    print(yaml.dump(client_config))


def _version(_: argparse.Namespace):
    print(f'racetrack-client version {__version__}')


def _login(args: argparse.Namespace):
    client_config: ClientConfig = load_client_config()
    set_user_auth(client_config, args.racetrack_url, args.user_token)
    save_client_config(client_config)
    logger.info(f'Logged to Racetrack: {args.racetrack_url}')


def _logout(args: argparse.Namespace):
    client_config: ClientConfig = load_client_config()
    set_user_auth(client_config, args.racetrack_url, "")
    save_client_config(client_config)
    logger.info(f'Logged out from Racetrack: {args.racetrack_url}')
