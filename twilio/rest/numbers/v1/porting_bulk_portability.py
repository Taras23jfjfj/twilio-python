r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PortingBulkPortabilityInstance(InstanceResource):
    class Status(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        EXPIRED = "expired"

    """
    :ivar sid: A 34 character string that uniquely identifies this Portability check.
    :ivar status: 
    :ivar datetime_created: The date that the Portability check was created, given in ISO 8601 format.
    :ivar phone_numbers: Contains a list with all the information of the requested phone numbers. Each phone number contains the following properties: `phone_number`: The phone number which portability is to be checked. `portable`: Boolean flag specifying if phone number is portable or not. `not_portable_reason`: Reason why the phone number cannot be ported into Twilio, `null` otherwise. `not_portable_reason_code`: The Portability Reason Code for the phone number if it cannot be ported in Twilio, `null` otherwise. `pin_and_account_number_required`: Boolean flag specifying if PIN and account number is required for the phone number. `number_type`: The type of the requested phone number. `country` Country the phone number belongs to. `messaging_carrier` Current messaging carrier of the phone number. `voice_carrier` Current voice carrier of the phone number.
    :ivar url: This is the url of the request that you're trying to reach out to locate the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["PortingBulkPortabilityInstance.Status"] = payload.get(
            "status"
        )
        self.datetime_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("datetime_created")
        )
        self.phone_numbers: Optional[List[object]] = payload.get("phone_numbers")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[PortingBulkPortabilityContext] = None

    @property
    def _proxy(self) -> "PortingBulkPortabilityContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PortingBulkPortabilityContext for this PortingBulkPortabilityInstance
        """
        if self._context is None:
            self._context = PortingBulkPortabilityContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "PortingBulkPortabilityInstance":
        """
        Fetch the PortingBulkPortabilityInstance


        :returns: The fetched PortingBulkPortabilityInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PortingBulkPortabilityInstance":
        """
        Asynchronous coroutine to fetch the PortingBulkPortabilityInstance


        :returns: The fetched PortingBulkPortabilityInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingBulkPortabilityInstance {}>".format(context)


class PortingBulkPortabilityContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the PortingBulkPortabilityContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies the Portability check.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Porting/Portability/{sid}".format(**self._solution)

    def fetch(self) -> PortingBulkPortabilityInstance:
        """
        Fetch the PortingBulkPortabilityInstance


        :returns: The fetched PortingBulkPortabilityInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PortingBulkPortabilityInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> PortingBulkPortabilityInstance:
        """
        Asynchronous coroutine to fetch the PortingBulkPortabilityInstance


        :returns: The fetched PortingBulkPortabilityInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PortingBulkPortabilityInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingBulkPortabilityContext {}>".format(context)


class PortingBulkPortabilityList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PortingBulkPortabilityList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Porting/Portability"

    def create(self, phone_numbers: List[str]) -> PortingBulkPortabilityInstance:
        """
        Create the PortingBulkPortabilityInstance

        :param phone_numbers: The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). .

        :returns: The created PortingBulkPortabilityInstance
        """
        data = values.of(
            {
                "PhoneNumbers": serialize.map(phone_numbers, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PortingBulkPortabilityInstance(self._version, payload)

    async def create_async(
        self, phone_numbers: List[str]
    ) -> PortingBulkPortabilityInstance:
        """
        Asynchronously create the PortingBulkPortabilityInstance

        :param phone_numbers: The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). .

        :returns: The created PortingBulkPortabilityInstance
        """
        data = values.of(
            {
                "PhoneNumbers": serialize.map(phone_numbers, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PortingBulkPortabilityInstance(self._version, payload)

    def get(self, sid: str) -> PortingBulkPortabilityContext:
        """
        Constructs a PortingBulkPortabilityContext

        :param sid: A 34 character string that uniquely identifies the Portability check.
        """
        return PortingBulkPortabilityContext(self._version, sid=sid)

    def __call__(self, sid: str) -> PortingBulkPortabilityContext:
        """
        Constructs a PortingBulkPortabilityContext

        :param sid: A 34 character string that uniquely identifies the Portability check.
        """
        return PortingBulkPortabilityContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.PortingBulkPortabilityList>"
