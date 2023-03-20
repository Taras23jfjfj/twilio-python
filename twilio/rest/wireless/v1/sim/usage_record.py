r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UsageRecordInstance(InstanceResource):
    class Granularity(object):
        HOURLY = "hourly"
        DAILY = "daily"
        ALL = "all"

    def __init__(self, version, payload, sim_sid: str):
        """
        Initialize the UsageRecordInstance

        :returns: twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance
        """
        super().__init__(version)

        self._properties = {
            "sim_sid": payload.get("sim_sid"),
            "account_sid": payload.get("account_sid"),
            "period": payload.get("period"),
            "commands": payload.get("commands"),
            "data": payload.get("data"),
        }

        self._solution = {
            "sim_sid": sim_sid,
        }

    @property
    def sim_sid(self):
        """
        :returns: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource) that this Usage Record is for.
        :rtype: str
        """
        return self._properties["sim_sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def period(self):
        """
        :returns: The time period for which the usage is reported. Contains `start` and `end` datetime values given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: dict
        """
        return self._properties["period"]

    @property
    def commands(self):
        """
        :returns: An object that describes the SIM's usage of Commands during the specified period. See [Commands Usage Object](https://www.twilio.com/docs/wireless/api/sim-usagerecord-resource#commands-usage-object).
        :rtype: dict
        """
        return self._properties["commands"]

    @property
    def data(self):
        """
        :returns: An object that describes the SIM's data usage during the specified period. See [Data Usage Object](https://www.twilio.com/docs/wireless/api/sim-usagerecord-resource#data-usage-object).
        :rtype: dict
        """
        return self._properties["data"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.UsageRecordInstance {}>".format(context)


class UsageRecordPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of UsageRecordInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance
        """
        return UsageRecordInstance(
            self._version, payload, sim_sid=self._solution["sim_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.UsageRecordPage>"


class UsageRecordList(ListResource):
    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the UsageRecordList

        :param Version version: Version that contains the resource
        :param sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource)  to read the usage from.

        :returns: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sim_sid": sim_sid,
        }
        self._uri = "/Sims/{sim_sid}/UsageRecords".format(**self._solution)

    def stream(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end=end, start=start, granularity=granularity, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            end=end, start=start, granularity=granularity, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance]
        """
        return list(
            self.stream(
                end=end,
                start=start,
                granularity=granularity,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.usage_record.UsageRecordInstance]
        """
        return list(
            await self.stream_async(
                end=end,
                start=start,
                granularity=granularity,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordPage
        """
        data = values.of(
            {
                "End": serialize.iso8601_datetime(end),
                "Start": serialize.iso8601_datetime(start),
                "Granularity": granularity,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UsageRecordPage(self._version, response, self._solution)

    async def page_async(
        self,
        end=values.unset,
        start=values.unset,
        granularity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param UsageRecordInstance.Granularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordPage
        """
        data = values.of(
            {
                "End": serialize.iso8601_datetime(end),
                "Start": serialize.iso8601_datetime(start),
                "Granularity": granularity,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UsageRecordPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UsageRecordPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.sim.usage_record.UsageRecordPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UsageRecordPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Wireless.V1.UsageRecordList>"
