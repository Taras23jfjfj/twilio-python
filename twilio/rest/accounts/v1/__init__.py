r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.accounts.v1.auth_token_promotion import AuthTokenPromotionList
from twilio.rest.accounts.v1.credential import CredentialList
from twilio.rest.accounts.v1.secondary_auth_token import SecondaryAuthTokenList


class V1(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Accounts

        :param domain: The Twilio.accounts domain
        """
        super().__init__(domain, "v1")
        self._auth_token_promotion: Optional[AuthTokenPromotionList] = None
        self._credentials: Optional[CredentialList] = None
        self._secondary_auth_token: Optional[SecondaryAuthTokenList] = None

    @property
    def auth_token_promotion(self) -> AuthTokenPromotionList:
        if self._auth_token_promotion is None:
            self._auth_token_promotion = AuthTokenPromotionList(self)
        return self._auth_token_promotion

    @property
    def credentials(self) -> CredentialList:
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def secondary_auth_token(self) -> SecondaryAuthTokenList:
        if self._secondary_auth_token is None:
            self._secondary_auth_token = SecondaryAuthTokenList(self)
        return self._secondary_auth_token

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Accounts.V1>"
