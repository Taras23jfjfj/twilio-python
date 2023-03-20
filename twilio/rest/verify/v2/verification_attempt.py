r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class VerificationAttemptList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptList
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptList
        """
        super().__init__(version)

        self._uri = "/Attempts"

    def stream(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams VerificationAttemptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams VerificationAttemptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists VerificationAttemptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance]
        """
        return list(
            self.stream(
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                channel_data_to=channel_data_to,
                country=country,
                channel=channel,
                verify_service_sid=verify_service_sid,
                verification_sid=verification_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists VerificationAttemptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance]
        """
        return list(
            await self.stream_async(
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                channel_data_to=channel_data_to,
                country=country,
                channel=channel,
                verify_service_sid=verify_service_sid,
                verification_sid=verification_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptPage
        """
        data = values.of(
            {
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "ChannelData.To": channel_data_to,
                "Country": country,
                "Channel": channel,
                "VerifyServiceSid": verify_service_sid,
                "VerificationSid": verification_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return VerificationAttemptPage(self._version, response)

    async def page_async(
        self,
        date_created_after=values.unset,
        date_created_before=values.unset,
        channel_data_to=values.unset,
        country=values.unset,
        channel=values.unset,
        verify_service_sid=values.unset,
        verification_sid=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param datetime date_created_after: Datetime filter used to query Verification Attempts created after this datetime. Given as GMT in RFC 2822 format.
        :param datetime date_created_before: Datetime filter used to query Verification Attempts created before this datetime. Given as GMT in RFC 2822 format.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param VerificationAttemptInstance.Channels channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param VerificationAttemptInstance.ConversionStatus status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptPage
        """
        data = values.of(
            {
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "ChannelData.To": channel_data_to,
                "Country": country,
                "Channel": channel,
                "VerifyServiceSid": verify_service_sid,
                "VerificationSid": verification_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return VerificationAttemptPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return VerificationAttemptPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return VerificationAttemptPage(self._version, response)

    def get(self, sid):
        """
        Constructs a VerificationAttemptContext

        :param sid: The unique SID identifier of a Verification Attempt

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        """
        return VerificationAttemptContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a VerificationAttemptContext

        :param sid: The unique SID identifier of a Verification Attempt

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        """
        return VerificationAttemptContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Verify.V2.VerificationAttemptList>"


class VerificationAttemptPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of VerificationAttemptInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """
        return VerificationAttemptInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.VerificationAttemptPage>"


class VerificationAttemptInstance(InstanceResource):
    class Channels(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"

    class ConversionStatus(object):
        CONVERTED = "converted"
        UNCONVERTED = "unconverted"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the VerificationAttemptInstance

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "verification_sid": payload.get("verification_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "conversion_status": payload.get("conversion_status"),
            "channel": payload.get("channel"),
            "price": payload.get("price"),
            "channel_data": payload.get("channel_data"),
            "url": payload.get("url"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[VerificationAttemptContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationAttemptContext for this VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        """
        if self._context is None:
            self._context = VerificationAttemptContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The SID that uniquely identifies the verification attempt resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) used to generate the attempt.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def verification_sid(self):
        """
        :returns: The SID of the [Verification](https://www.twilio.com/docs/verify/api/verification) that generated the attempt.
        :rtype: str
        """
        return self._properties["verification_sid"]

    @property
    def date_created(self):
        """
        :returns: The date that this Attempt was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date that this Attempt was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def conversion_status(self):
        """
        :returns:
        :rtype: VerificationAttemptInstance.ConversionStatus
        """
        return self._properties["conversion_status"]

    @property
    def channel(self):
        """
        :returns:
        :rtype: VerificationAttemptInstance.Channels
        """
        return self._properties["channel"]

    @property
    def price(self):
        """
        :returns: An object containing the charge for this verification attempt related to the channel costs and the currency used. The costs related to the succeeded verifications are not included. May not be immediately available. More information on pricing is available [here](https://www.twilio.com/verify/pricing).
        :rtype: dict
        """
        return self._properties["price"]

    @property
    def channel_data(self):
        """
        :returns: An object containing the channel specific information for an attempt.
        :rtype: dict
        """
        return self._properties["channel_data"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the VerificationAttemptInstance


        :returns: The fetched VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VerificationAttemptInstance


        :returns: The fetched VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.VerificationAttemptInstance {}>".format(context)


class VerificationAttemptContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the VerificationAttemptContext

        :param Version version: Version that contains the resource
        :param sid: The unique SID identifier of a Verification Attempt

        :returns: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Attempts/{sid}".format(**self._solution)

    def fetch(self):
        """
        Fetch the VerificationAttemptInstance


        :returns: The fetched VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return VerificationAttemptInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VerificationAttemptInstance


        :returns: The fetched VerificationAttemptInstance
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return VerificationAttemptInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.VerificationAttemptContext {}>".format(context)
