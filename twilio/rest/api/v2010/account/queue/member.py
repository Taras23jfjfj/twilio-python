r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class MemberInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        account_sid: str,
        queue_sid: str,
        call_sid: Optional[str] = None,
    ):
        """
        Initialize the MemberInstance

        :returns: twilio.rest.api.v2010.account.queue.member.MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        super().__init__(version)

        self._properties = {
            "call_sid": payload.get("call_sid"),
            "date_enqueued": deserialize.rfc2822_datetime(payload.get("date_enqueued")),
            "position": deserialize.integer(payload.get("position")),
            "uri": payload.get("uri"),
            "wait_time": deserialize.integer(payload.get("wait_time")),
            "queue_sid": payload.get("queue_sid"),
        }

        self._solution = {
            "account_sid": account_sid,
            "queue_sid": queue_sid,
            "call_sid": call_sid or self._properties["call_sid"],
        }
        self._context: Optional[MemberContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MemberContext for this MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberContext
        """
        if self._context is None:
            self._context = MemberContext(
                self._version,
                account_sid=self._solution["account_sid"],
                queue_sid=self._solution["queue_sid"],
                call_sid=self._solution["call_sid"],
            )
        return self._context

    @property
    def call_sid(self):
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Member resource is associated with.
        :rtype: str
        """
        return self._properties["call_sid"]

    @property
    def date_enqueued(self):
        """
        :returns: The date that the member was enqueued, given in RFC 2822 format.
        :rtype: datetime
        """
        return self._properties["date_enqueued"]

    @property
    def position(self):
        """
        :returns: This member's current position in the queue.
        :rtype: int
        """
        return self._properties["position"]

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties["uri"]

    @property
    def wait_time(self):
        """
        :returns: The number of seconds the member has been in the queue.
        :rtype: int
        """
        return self._properties["wait_time"]

    @property
    def queue_sid(self):
        """
        :returns: The SID of the Queue the member is in.
        :rtype: str
        """
        return self._properties["queue_sid"]

    def fetch(self):
        """
        Fetch the MemberInstance


        :returns: The fetched MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the MemberInstance


        :returns: The fetched MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        return await self._proxy.fetch_async()

    def update(self, url, method=values.unset):
        """
        Update the MemberInstance

        :param str url: The absolute URL of the Queue resource.
        :param str method: How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        return self._proxy.update(
            url=url,
            method=method,
        )

    async def update_async(self, url, method=values.unset):
        """
        Asynchronous coroutine to update the MemberInstance

        :param str url: The absolute URL of the Queue resource.
        :param str method: How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        return await self._proxy.update_async(
            url=url,
            method=method,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.MemberInstance {}>".format(context)


class MemberContext(InstanceContext):
    def __init__(
        self, version: Version, account_sid: str, queue_sid: str, call_sid: str
    ):
        """
        Initialize the MemberContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update.
        :param queue_sid: The SID of the Queue in which to find the members to update.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.

        :returns: twilio.rest.api.v2010.account.queue.member.MemberContext
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "queue_sid": queue_sid,
            "call_sid": call_sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json".format(
                **self._solution
            )
        )

    def fetch(self):
        """
        Fetch the MemberInstance


        :returns: The fetched MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MemberInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the MemberInstance


        :returns: The fetched MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MemberInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=self._solution["call_sid"],
        )

    def update(self, url, method=values.unset):
        """
        Update the MemberInstance

        :param str url: The absolute URL of the Queue resource.
        :param str method: How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        data = values.of(
            {
                "Url": url,
                "Method": method,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def update_async(self, url, method=values.unset):
        """
        Asynchronous coroutine to update the MemberInstance

        :param str url: The absolute URL of the Queue resource.
        :param str method: How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        data = values.of(
            {
                "Url": url,
                "Method": method,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=self._solution["call_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.MemberContext {}>".format(context)


class MemberPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of MemberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.queue.member.MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberInstance
        """
        return MemberInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.MemberPage>"


class MemberList(ListResource):
    def __init__(self, version: Version, account_sid: str, queue_sid: str):
        """
        Initialize the MemberList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read.
        :param queue_sid: The SID of the Queue in which to find the members

        :returns: twilio.rest.api.v2010.account.queue.member.MemberList
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "queue_sid": queue_sid,
        }
        self._uri = "/Accounts/{account_sid}/Queues/{queue_sid}/Members.json".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams MemberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.queue.member.MemberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams MemberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.queue.member.MemberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.queue.member.MemberInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.queue.member.MemberInstance]
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
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MemberPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of MemberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberPage
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
        return MemberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MemberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MemberPage(self._version, response, self._solution)

    def get(self, call_sid):
        """
        Constructs a MemberContext

        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.

        :returns: twilio.rest.api.v2010.account.queue.member.MemberContext
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberContext
        """
        return MemberContext(
            self._version,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=call_sid,
        )

    def __call__(self, call_sid):
        """
        Constructs a MemberContext

        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.

        :returns: twilio.rest.api.v2010.account.queue.member.MemberContext
        :rtype: twilio.rest.api.v2010.account.queue.member.MemberContext
        """
        return MemberContext(
            self._version,
            account_sid=self._solution["account_sid"],
            queue_sid=self._solution["queue_sid"],
            call_sid=call_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.MemberList>"
