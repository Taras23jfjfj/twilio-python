r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AssessmentsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AssessmentsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsList
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Insights/QM/Assessments".format(**self._solution)

    def create(
        self,
        category_id,
        category_name,
        segment_id,
        user_name,
        user_email,
        agent_id,
        offset,
        metric_id,
        metric_name,
        answer_text,
        answer_id,
        questionnaire_id,
        token=values.unset,
    ):
        """
        Create the AssessmentsInstance

        :param str category_id: The id of the category
        :param str category_name: The name of the category
        :param str segment_id: Segment Id of the conversation
        :param str user_name: Name of the user assessing conversation
        :param str user_email: Email of the user assessing conversation
        :param str agent_id: The id of the Agent
        :param float offset: The offset of the conversation.
        :param str metric_id: The question Id selected for assessment
        :param str metric_name: The question name of the assessment
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str questionnaire_id: Questionnaire Id of the associated question
        :param str token: The Token HTTP request header

        :returns: The created AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
                "MetricId": metric_id,
                "MetricName": metric_name,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
                "QuestionnaireId": questionnaire_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(self._version, payload)

    async def create_async(
        self,
        category_id,
        category_name,
        segment_id,
        user_name,
        user_email,
        agent_id,
        offset,
        metric_id,
        metric_name,
        answer_text,
        answer_id,
        questionnaire_id,
        token=values.unset,
    ):
        """
        Asynchronously create the AssessmentsInstance

        :param str category_id: The id of the category
        :param str category_name: The name of the category
        :param str segment_id: Segment Id of the conversation
        :param str user_name: Name of the user assessing conversation
        :param str user_email: Email of the user assessing conversation
        :param str agent_id: The id of the Agent
        :param float offset: The offset of the conversation.
        :param str metric_id: The question Id selected for assessment
        :param str metric_name: The question name of the assessment
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str questionnaire_id: Questionnaire Id of the associated question
        :param str token: The Token HTTP request header

        :returns: The created AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
                "MetricId": metric_id,
                "MetricName": metric_name,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
                "QuestionnaireId": questionnaire_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(self._version, payload)

    def stream(
        self, token=values.unset, segment_id=values.unset, limit=None, page_size=None
    ):
        """
        Streams AssessmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.assessments.AssessmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token, segment_id=segment_id, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, token=values.unset, segment_id=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously streams AssessmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.assessments.AssessmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            token=token, segment_id=segment_id, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, token=values.unset, segment_id=values.unset, limit=None, page_size=None
    ):
        """
        Lists AssessmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.assessments.AssessmentsInstance]
        """
        return list(
            self.stream(
                token=token,
                segment_id=segment_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, token=values.unset, segment_id=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously lists AssessmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.assessments.AssessmentsInstance]
        """
        return list(
            await self.stream_async(
                token=token,
                segment_id=segment_id,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        token=values.unset,
        segment_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssessmentsPage(self._version, response, self._solution)

    async def page_async(
        self,
        token=values.unset,
        segment_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AssessmentsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssessmentsPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssessmentsPage(self._version, response, self._solution)

    def get(self, assessment_id):
        """
        Constructs a AssessmentsContext

        :param assessment_id: The id of the assessment to be modified

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        return AssessmentsContext(self._version, assessment_id=assessment_id)

    def __call__(self, assessment_id):
        """
        Constructs a AssessmentsContext

        :param assessment_id: The id of the assessment to be modified

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        return AssessmentsContext(self._version, assessment_id=assessment_id)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.AssessmentsList>"


class AssessmentsPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the AssessmentsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssessmentsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        return AssessmentsInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.AssessmentsPage>"


class AssessmentsInstance(InstanceResource):
    def __init__(self, version, payload, assessment_id: str = None):
        """
        Initialize the AssessmentsInstance

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "assessment_id": payload.get("assessment_id"),
            "offset": deserialize.decimal(payload.get("offset")),
            "report": payload.get("report"),
            "weight": deserialize.decimal(payload.get("weight")),
            "agent_id": payload.get("agent_id"),
            "segment_id": payload.get("segment_id"),
            "user_name": payload.get("user_name"),
            "user_email": payload.get("user_email"),
            "answer_text": payload.get("answer_text"),
            "answer_id": payload.get("answer_id"),
            "assessment": payload.get("assessment"),
            "timestamp": deserialize.decimal(payload.get("timestamp")),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "assessment_id": assessment_id or self._properties["assessment_id"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssessmentsContext for this AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        if self._context is None:
            self._context = AssessmentsContext(
                self._version,
                assessment_id=self._solution["assessment_id"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def assessment_id(self):
        """
        :returns: The unique id of the assessment
        :rtype: str
        """
        return self._properties["assessment_id"]

    @property
    def offset(self):
        """
        :returns: Offset of the conversation
        :rtype: float
        """
        return self._properties["offset"]

    @property
    def report(self):
        """
        :returns: The flag indicating if this assessment is part of report
        :rtype: bool
        """
        return self._properties["report"]

    @property
    def weight(self):
        """
        :returns: The weightage given to this comment
        :rtype: float
        """
        return self._properties["weight"]

    @property
    def agent_id(self):
        """
        :returns: The id of the Agent
        :rtype: str
        """
        return self._properties["agent_id"]

    @property
    def segment_id(self):
        """
        :returns: Segment Id of conversation
        :rtype: str
        """
        return self._properties["segment_id"]

    @property
    def user_name(self):
        """
        :returns: The name of the user.
        :rtype: str
        """
        return self._properties["user_name"]

    @property
    def user_email(self):
        """
        :returns: The email id of the user.
        :rtype: str
        """
        return self._properties["user_email"]

    @property
    def answer_text(self):
        """
        :returns: The answer text selected by user
        :rtype: str
        """
        return self._properties["answer_text"]

    @property
    def answer_id(self):
        """
        :returns: The id of the answer selected by user
        :rtype: str
        """
        return self._properties["answer_id"]

    @property
    def assessment(self):
        """
        :returns: Assessment Details associated with an assessment
        :rtype: dict
        """
        return self._properties["assessment"]

    @property
    def timestamp(self):
        """
        :returns:
        :rtype: float
        """
        return self._properties["timestamp"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def update(self, offset, answer_text, answer_id, token=values.unset):
        """
        Update the AssessmentsInstance

        :param float offset: The offset of the conversation
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        return self._proxy.update(
            offset=offset,
            answer_text=answer_text,
            answer_id=answer_id,
            token=token,
        )

    async def update_async(self, offset, answer_text, answer_id, token=values.unset):
        """
        Asynchronous coroutine to update the AssessmentsInstance

        :param float offset: The offset of the conversation
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        return await self._proxy.update_async(
            offset=offset,
            answer_text=answer_text,
            answer_id=answer_id,
            token=token,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.AssessmentsInstance {}>".format(context)


class AssessmentsContext(InstanceContext):
    def __init__(self, version: Version, assessment_id: str):
        """
        Initialize the AssessmentsContext

        :param Version version: Version that contains the resource
        :param assessment_id: The id of the assessment to be modified

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assessment_id": assessment_id,
        }
        self._uri = "/Insights/QM/Assessments/{assessment_id}".format(**self._solution)

    def update(self, offset, answer_text, answer_id, token=values.unset):
        """
        Update the AssessmentsInstance

        :param float offset: The offset of the conversation
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        data = values.of(
            {
                "Offset": offset,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(
            self._version, payload, assessment_id=self._solution["assessment_id"]
        )

    async def update_async(self, offset, answer_text, answer_id, token=values.unset):
        """
        Asynchronous coroutine to update the AssessmentsInstance

        :param float offset: The offset of the conversation
        :param str answer_text: The answer text selected by user
        :param str answer_id: The id of the answer selected by user
        :param str token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        data = values.of(
            {
                "Offset": offset,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(
            self._version, payload, assessment_id=self._solution["assessment_id"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.AssessmentsContext {}>".format(context)
