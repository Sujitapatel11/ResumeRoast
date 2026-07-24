"""
Authentication-related constants used across the auth module.
"""

from enum import StrEnum


class UserRole(StrEnum):
    """
    Defines the roles available in the application.
    """

    USER = "user"
    ADMIN = "admin"


class TokenType(StrEnum):
    """
    Defines the supported JWT token types.
    """

    ACCESS = "access"
    REFRESH = "refresh"
    EMAIL_VERIFICATION = "email_verification"
    PASSWORD_RESET = "password_reset"


class OAuthProvider(StrEnum):
    """
    Supported OAuth providers.
    """

    GOOGLE = "google"


class AccountStatus(StrEnum):
    """
    Current account status.
    """

    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"


# Password Policy
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128


# User Limits
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 100


# Email Limits
MAX_EMAIL_LENGTH = 254