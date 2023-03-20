r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DayInstance(InstanceResource):
    def __init__(self, version, payload, resource_type: str, day: Optional[str] = None):
        """
        Initialize the DayInstance

        :returns: twilio.rest.bulkexports.v1.export.day.DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """
        super().__init__(version)

        self._properties = {
            "redirect_to": payload.get("redirect_to"),
            "day": payload.get("day"),
            "size": deserialize.integer(payload.get("size")),
            "create_date": payload.get("create_date"),
            "friendly_name": payload.get("friendly_name"),
            "resource_type": payload.get("resource_type"),
        }

        self._solution = {
            "resource_type": resource_type,
            "day": day or self._properties["day"],
        }
        self._context: Optional[DayContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DayContext for this DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayContext
        """
        if self._context is None:
            self._context = DayContext(
                self._version,
                resource_type=self._solution["resource_type"],
                day=self._solution["day"],
            )
        return self._context

    @property
    def redirect_to(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["redirect_to"]

    @property
    def day(self):
        """
        :returns: The ISO 8601 format date of the resources in the file, for a UTC day
        :rtype: str
        """
        return self._properties["day"]

    @property
    def size(self):
        """
        :returns: The size of the day's data file in bytes
        :rtype: int
        """
        return self._properties["size"]

    @property
    def create_date(self):
        """
        :returns: The ISO 8601 format date when resources is created
        :rtype: str
        """
        return self._properties["create_date"]

    @property
    def friendly_name(self):
        """
        :returns: The friendly name specified when creating the job
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def resource_type(self):
        """
        :returns: The type of communication – Messages, Calls, Conferences, and Participants
        :rtype: str
        """
        return self._properties["resource_type"]

    def fetch(self):
        """
        Fetch the DayInstance


        :returns: The fetched DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DayInstance


        :returns: The fetched DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Bulkexports.V1.DayInstance {}>".format(context)


class DayContext(InstanceContext):
    def __init__(self, version: Version, resource_type: str, day: str):
        """
        Initialize the DayContext

        :param Version version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
        :param day: The ISO 8601 format date of the resources in the file, for a UTC day

        :returns: twilio.rest.bulkexports.v1.export.day.DayContext
        :rtype: twilio.rest.bulkexports.v1.export.day.DayContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "resource_type": resource_type,
            "day": day,
        }
        self._uri = "/Exports/{resource_type}/Days/{day}".format(**self._solution)

    def fetch(self):
        """
        Fetch the DayInstance


        :returns: The fetched DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DayInstance(
            self._version,
            payload,
            resource_type=self._solution["resource_type"],
            day=self._solution["day"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DayInstance


        :returns: The fetched DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DayInstance(
            self._version,
            payload,
            resource_type=self._solution["resource_type"],
            day=self._solution["day"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Bulkexports.V1.DayContext {}>".format(context)


class DayPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of DayInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.bulkexports.v1.export.day.DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayInstance
        """
        return DayInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Bulkexports.V1.DayPage>"


class DayList(ListResource):
    def __init__(self, version: Version, resource_type: str):
        """
        Initialize the DayList

        :param Version version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants

        :returns: twilio.rest.bulkexports.v1.export.day.DayList
        :rtype: twilio.rest.bulkexports.v1.export.day.DayList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "resource_type": resource_type,
        }
        self._uri = "/Exports/{resource_type}/Days".format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DayInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.day.DayInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams DayInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.day.DayInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists DayInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.day.DayInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists DayInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.day.DayInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of DayInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DayPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of DayInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DayPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DayInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DayPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of DayInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DayInstance
        :rtype: twilio.rest.bulkexports.v1.export.day.DayPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DayPage(self._version, response, self._solution)

    def get(self, day):
        """
        Constructs a DayContext

        :param day: The ISO 8601 format date of the resources in the file, for a UTC day

        :returns: twilio.rest.bulkexports.v1.export.day.DayContext
        :rtype: twilio.rest.bulkexports.v1.export.day.DayContext
        """
        return DayContext(
            self._version, resource_type=self._solution["resource_type"], day=day
        )

    def __call__(self, day):
        """
        Constructs a DayContext

        :param day: The ISO 8601 format date of the resources in the file, for a UTC day

        :returns: twilio.rest.bulkexports.v1.export.day.DayContext
        :rtype: twilio.rest.bulkexports.v1.export.day.DayContext
        """
        return DayContext(
            self._version, resource_type=self._solution["resource_type"], day=day
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Bulkexports.V1.DayList>"
