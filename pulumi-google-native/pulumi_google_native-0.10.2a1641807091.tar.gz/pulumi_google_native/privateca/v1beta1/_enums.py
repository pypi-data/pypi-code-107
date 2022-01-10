# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'CertificateAuthorityTier',
    'CertificateAuthorityType',
    'KeyVersionSpecAlgorithm',
    'PublicKeyType',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """
    Default case. Should never be this.
    """
    ADMIN_READ = "ADMIN_READ"
    """
    Admin reads. Example: CloudIAM getIamPolicy
    """
    DATA_WRITE = "DATA_WRITE"
    """
    Data writes. Example: CloudSQL Users create
    """
    DATA_READ = "DATA_READ"
    """
    Data reads. Example: CloudSQL Users list
    """


class CertificateAuthorityTier(str, Enum):
    """
    Required. Immutable. The Tier of this CertificateAuthority.
    """
    TIER_UNSPECIFIED = "TIER_UNSPECIFIED"
    """
    Not specified.
    """
    ENTERPRISE = "ENTERPRISE"
    """
    Enterprise tier.
    """
    DEVOPS = "DEVOPS"
    """
    DevOps tier.
    """


class CertificateAuthorityType(str, Enum):
    """
    Required. Immutable. The Type of this CertificateAuthority.
    """
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    """
    Not specified.
    """
    SELF_SIGNED = "SELF_SIGNED"
    """
    Self-signed CA.
    """
    SUBORDINATE = "SUBORDINATE"
    """
    Subordinate CA. Could be issued by a Private CA CertificateAuthority or an unmanaged CA.
    """


class KeyVersionSpecAlgorithm(str, Enum):
    """
    Required. The algorithm to use for creating a managed Cloud KMS key for a for a simplified experience. All managed keys will be have their ProtectionLevel as `HSM`.
    """
    SIGN_HASH_ALGORITHM_UNSPECIFIED = "SIGN_HASH_ALGORITHM_UNSPECIFIED"
    """
    Not specified.
    """
    RSA_PSS2048_SHA256 = "RSA_PSS_2048_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256
    """
    RSA_PSS3072_SHA256 = "RSA_PSS_3072_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm. RSA_SIGN_PSS_3072_SHA256
    """
    RSA_PSS4096_SHA256 = "RSA_PSS_4096_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_4096_SHA256
    """
    RSA_PKCS12048_SHA256 = "RSA_PKCS1_2048_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_2048_SHA256
    """
    RSA_PKCS13072_SHA256 = "RSA_PKCS1_3072_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_3072_SHA256
    """
    RSA_PKCS14096_SHA256 = "RSA_PKCS1_4096_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_4096_SHA256
    """
    EC_P256_SHA256 = "EC_P256_SHA256"
    """
    maps to CryptoKeyVersionAlgorithm.EC_SIGN_P256_SHA256
    """
    EC_P384_SHA384 = "EC_P384_SHA384"
    """
    maps to CryptoKeyVersionAlgorithm.EC_SIGN_P384_SHA384
    """


class PublicKeyType(str, Enum):
    """
    Optional. The type of public key. If specified, it must match the public key used for the`key` field.
    """
    KEY_TYPE_UNSPECIFIED = "KEY_TYPE_UNSPECIFIED"
    """
    Default unspecified value.
    """
    PEM_RSA_KEY = "PEM_RSA_KEY"
    """
    A PEM-encoded PKCS#1/RFC 3447 RSAPublicKey structure, or an RFC 5280 [SubjectPublicKeyInfo](https://tools.ietf.org/html/rfc5280#section-4.1) structure containing the former.
    """
    PEM_EC_KEY = "PEM_EC_KEY"
    """
    An RFC 5280 [SubjectPublicKeyInfo](https://tools.ietf.org/html/rfc5280#section-4.1) structure containing a PEM-encoded compressed NIST P-256/secp256r1/prime256v1 or P-384 key.
    """
