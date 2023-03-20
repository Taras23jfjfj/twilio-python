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


from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ExportCustomJobList(ListResource):
    def __init__(self, version: Version, resource_type: str):
        """
        Initialize the ExportCustomJobList

        :param Version version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants

        :returns: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobList
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "resource_type": resource_type,
        }
        self._uri = "/Exports/{resource_type}/Jobs".format(**self._solution)

    def create(
        self,
        start_day,
        end_day,
        friendly_name,
        webhook_url=values.unset,
        webhook_method=values.unset,
        email=values.unset,
    ):
        """
        Create the ExportCustomJobInstance

        :param str start_day: The start day for the custom export specified as a string in the format of yyyy-mm-dd
        :param str end_day: The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
        :param str friendly_name: The friendly name specified when creating the job
        :param str webhook_url: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
        :param str webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
        :param str email: The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.

        :returns: The created ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        """
        data = values.of(
            {
                "StartDay": start_day,
                "EndDay": end_day,
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "WebhookMethod": webhook_method,
                "Email": email,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    async def create_async(
        self,
        start_day,
        end_day,
        friendly_name,
        webhook_url=values.unset,
        webhook_method=values.unset,
        email=values.unset,
    ):
        """
        Asynchronously create the ExportCustomJobInstance

        :param str start_day: The start day for the custom export specified as a string in the format of yyyy-mm-dd
        :param str end_day: The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
        :param str friendly_name: The friendly name specified when creating the job
        :param str webhook_url: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
        :param str webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
        :param str email: The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.

        :returns: The created ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        """
        data = values.of(
            {
                "StartDay": start_day,
                "EndDay": end_day,
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "WebhookMethod": webhook_method,
                "Email": email,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams ExportCustomJobInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams ExportCustomJobInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists ExportCustomJobInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists ExportCustomJobInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance]
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
        Retrieve a single page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ExportCustomJobPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobPage
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
        return ExportCustomJobPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ExportCustomJobPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ExportCustomJobPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Bulkexports.V1.ExportCustomJobList>"


class ExportCustomJobPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of ExportCustomJobInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        """
        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Bulkexports.V1.ExportCustomJobPage>"


class ExportCustomJobInstance(InstanceResource):
    def __init__(self, version, payload, resource_type: str):
        """
        Initialize the ExportCustomJobInstance

        :returns: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        :rtype: twilio.rest.bulkexports.v1.export.export_custom_job.ExportCustomJobInstance
        """
        super().__init__(version)

        self._properties = {
            "friendly_name": payload.get("friendly_name"),
            "resource_type": payload.get("resource_type"),
            "start_day": payload.get("start_day"),
            "end_day": payload.get("end_day"),
            "webhook_url": payload.get("webhook_url"),
            "webhook_method": payload.get("webhook_method"),
            "email": payload.get("email"),
            "job_sid": payload.get("job_sid"),
            "details": payload.get("details"),
            "job_queue_position": payload.get("job_queue_position"),
            "estimated_completion_time": payload.get("estimated_completion_time"),
        }

        self._solution = {
            "resource_type": resource_type,
        }

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

    @property
    def start_day(self):
        """
        :returns: The start day for the custom export specified when creating the job
        :rtype: str
        """
        return self._properties["start_day"]

    @property
    def end_day(self):
        """
        :returns: The end day for the export specified when creating the job
        :rtype: str
        """
        return self._properties["end_day"]

    @property
    def webhook_url(self):
        """
        :returns: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied.
        :rtype: str
        """
        return self._properties["webhook_url"]

    @property
    def webhook_method(self):
        """
        :returns: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
        :rtype: str
        """
        return self._properties["webhook_method"]

    @property
    def email(self):
        """
        :returns: The optional email to send the completion notification to
        :rtype: str
        """
        return self._properties["email"]

    @property
    def job_sid(self):
        """
        :returns: The unique job_sid returned when the custom export was created
        :rtype: str
        """
        return self._properties["job_sid"]

    @property
    def details(self):
        """
        :returns: The details of a job which is an object that contains an array of status grouped by `status` state.  Each `status` object has a `status` string, a count which is the number of days in that `status`, and list of days in that `status`. The day strings are in the format yyyy-MM-dd. As an example, a currently running job may have a status object for COMPLETED and a `status` object for SUBMITTED each with its own count and list of days.
        :rtype: dict
        """
        return self._properties["details"]

    @property
    def job_queue_position(self):
        """
        :returns: This is the job position from the 1st in line. Your queue position will never increase. As jobs ahead of yours in the queue are processed, the queue position number will decrease
        :rtype: str
        """
        return self._properties["job_queue_position"]

    @property
    def estimated_completion_time(self):
        """
        :returns: this is the time estimated until your job is complete. This is calculated each time you request the job list. The time is calculated based on the current rate of job completion (which may vary) and your job queue position
        :rtype: str
        """
        return self._properties["estimated_completion_time"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Bulkexports.V1.ExportCustomJobInstance {}>".format(context)
