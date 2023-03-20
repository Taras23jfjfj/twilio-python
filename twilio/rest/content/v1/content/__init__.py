r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.content.v1.content.approval_fetch import ApprovalFetchList


class ContentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ContentList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.content.v1.content.ContentList
        :rtype: twilio.rest.content.v1.content.ContentList
        """
        super().__init__(version)

        self._uri = "/Content"

    def stream(self, limit=None, page_size=None):
        """
        Streams ContentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.content.v1.content.ContentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams ContentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.content.v1.content.ContentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.content.v1.content.ContentInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists ContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.content.v1.content.ContentInstance]
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
        Retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ContentPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of ContentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentPage
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
        return ContentPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ContentPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of ContentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ContentPage(self._version, response)

    def get(self, sid):
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.

        :returns: twilio.rest.content.v1.content.ContentContext
        :rtype: twilio.rest.content.v1.content.ContentContext
        """
        return ContentContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ContentContext

        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.

        :returns: twilio.rest.content.v1.content.ContentContext
        :rtype: twilio.rest.content.v1.content.ContentContext
        """
        return ContentContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Content.V1.ContentList>"


class ContentPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of ContentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.content.v1.content.ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """
        return ContentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentPage>"


class ContentInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the ContentInstance

        :returns: twilio.rest.content.v1.content.ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """
        super().__init__(version)

        self._properties = {
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "language": payload.get("language"),
            "variables": payload.get("variables"),
            "types": payload.get("types"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[ContentContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ContentContext for this ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentContext
        """
        if self._context is None:
            self._context = ContentContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Content resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: A string name used to describe the Content resource. Not visible to the end recipient.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def language(self):
        """
        :returns: Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.
        :rtype: str
        """
        return self._properties["language"]

    @property
    def variables(self):
        """
        :returns: Defines the default placeholder values for variables included in the Content resource. e.g. {\"1\": \"Customer_Name\"}.
        :rtype: dict
        """
        return self._properties["variables"]

    @property
    def types(self):
        """
        :returns: The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.
        :rtype: dict
        """
        return self._properties["types"]

    @property
    def url(self):
        """
        :returns: The URL of the resource, relative to `https://content.twilio.com`.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: A list of links related to the Content resource, such as approval_fetch and approval_create
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """
        return await self._proxy.fetch_async()

    @property
    def approval_fetch(self):
        """
        Access the approval_fetch

        :returns: twilio.rest.content.v1.content.ApprovalFetchList
        :rtype: twilio.rest.content.v1.content.ApprovalFetchList
        """
        return self._proxy.approval_fetch

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentInstance {}>".format(context)


class ContentContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ContentContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.

        :returns: twilio.rest.content.v1.content.ContentContext
        :rtype: twilio.rest.content.v1.content.ContentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Content/{sid}".format(**self._solution)

        self._approval_fetch: Optional[ApprovalFetchList] = None

    def delete(self):
        """
        Deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ContentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the ContentInstance


        :returns: The fetched ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ContentInstance


        :returns: The fetched ContentInstance
        :rtype: twilio.rest.content.v1.content.ContentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ContentInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def approval_fetch(self):
        """
        Access the approval_fetch

        :returns: twilio.rest.content.v1.content.ApprovalFetchList
        :rtype: twilio.rest.content.v1.content.ApprovalFetchList
        """
        if self._approval_fetch is None:
            self._approval_fetch = ApprovalFetchList(
                self._version,
                self._solution["sid"],
            )
        return self._approval_fetch

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentContext {}>".format(context)
