r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EventInstance(InstanceResource):
    class Level(object):
        UNKNOWN = "UNKNOWN"
        DEBUG = "DEBUG"
        INFO = "INFO"
        WARNING = "WARNING"
        ERROR = "ERROR"

    class TwilioEdge(object):
        UNKNOWN_EDGE = "unknown_edge"
        CARRIER_EDGE = "carrier_edge"
        SIP_EDGE = "sip_edge"
        SDK_EDGE = "sdk_edge"
        CLIENT_EDGE = "client_edge"

    def __init__(self, version, payload, call_sid: str):
        """
        Initialize the EventInstance

        :returns: twilio.rest.insights.v1.call.event.EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventInstance
        """
        super().__init__(version)

        self._properties = {
            "timestamp": payload.get("timestamp"),
            "call_sid": payload.get("call_sid"),
            "account_sid": payload.get("account_sid"),
            "edge": payload.get("edge"),
            "group": payload.get("group"),
            "level": payload.get("level"),
            "name": payload.get("name"),
            "carrier_edge": payload.get("carrier_edge"),
            "sip_edge": payload.get("sip_edge"),
            "sdk_edge": payload.get("sdk_edge"),
            "client_edge": payload.get("client_edge"),
        }

        self._solution = {
            "call_sid": call_sid,
        }

    @property
    def timestamp(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["timestamp"]

    @property
    def call_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["call_sid"]

    @property
    def account_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def edge(self):
        """
        :returns:
        :rtype: EventInstance.TwilioEdge
        """
        return self._properties["edge"]

    @property
    def group(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["group"]

    @property
    def level(self):
        """
        :returns:
        :rtype: EventInstance.Level
        """
        return self._properties["level"]

    @property
    def name(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["name"]

    @property
    def carrier_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["carrier_edge"]

    @property
    def sip_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["sip_edge"]

    @property
    def sdk_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["sdk_edge"]

    @property
    def client_edge(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["client_edge"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.EventInstance {}>".format(context)


class EventPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of EventInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.call.event.EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventInstance
        """
        return EventInstance(
            self._version, payload, call_sid=self._solution["call_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.EventPage>"


class EventList(ListResource):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the EventList

        :param Version version: Version that contains the resource
        :param call_sid:

        :returns: twilio.rest.insights.v1.call.event.EventList
        :rtype: twilio.rest.insights.v1.call.event.EventList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }
        self._uri = "/Voice/{call_sid}/Events".format(**self._solution)

    def stream(self, edge=values.unset, limit=None, page_size=None):
        """
        Streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param EventInstance.TwilioEdge edge:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.event.EventInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(edge=edge, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, edge=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param EventInstance.TwilioEdge edge:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.event.EventInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(edge=edge, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, edge=values.unset, limit=None, page_size=None):
        """
        Lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param EventInstance.TwilioEdge edge:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.event.EventInstance]
        """
        return list(
            self.stream(
                edge=edge,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, edge=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param EventInstance.TwilioEdge edge:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.event.EventInstance]
        """
        return list(
            await self.stream_async(
                edge=edge,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        edge=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately

        :param EventInstance.TwilioEdge edge:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventPage
        """
        data = values.of(
            {
                "Edge": edge,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EventPage(self._version, response, self._solution)

    async def page_async(
        self,
        edge=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of EventInstance records from the API.
        Request is executed immediately

        :param EventInstance.TwilioEdge edge:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventPage
        """
        data = values.of(
            {
                "Edge": edge,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return EventPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EventPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        :rtype: twilio.rest.insights.v1.call.event.EventPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EventPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Insights.V1.EventList>"
