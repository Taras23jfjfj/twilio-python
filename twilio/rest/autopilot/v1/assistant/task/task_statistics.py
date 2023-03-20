r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskStatisticsList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsList
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }

    def get(self):
        """
        Constructs a TaskStatisticsContext


        :returns: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        """
        return TaskStatisticsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __call__(self):
        """
        Constructs a TaskStatisticsContext


        :returns: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        """
        return TaskStatisticsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Autopilot.V1.TaskStatisticsList>"


class TaskStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsInstance

        :returns: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "assistant_sid": payload.get("assistant_sid"),
            "task_sid": payload.get("task_sid"),
            "samples_count": deserialize.integer(payload.get("samples_count")),
            "fields_count": deserialize.integer(payload.get("fields_count")),
            "url": payload.get("url"),
        }

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._context: Optional[TaskStatisticsContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskStatisticsContext for this TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        """
        if self._context is None:
            self._context = TaskStatisticsContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskStatistics resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource.
        :rtype: str
        """
        return self._properties["assistant_sid"]

    @property
    def task_sid(self):
        """
        :returns: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the statistics were collected.
        :rtype: str
        """
        return self._properties["task_sid"]

    @property
    def samples_count(self):
        """
        :returns: The total number of [Samples](https://www.twilio.com/docs/autopilot/api/task-sample) associated with the Task.
        :rtype: int
        """
        return self._properties["samples_count"]

    @property
    def fields_count(self):
        """
        :returns: The total number of [Fields](https://www.twilio.com/docs/autopilot/api/task-field) associated with the Task.
        :rtype: int
        """
        return self._properties["fields_count"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the TaskStatistics resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.TaskStatisticsInstance {}>".format(context)


class TaskStatisticsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics".format(
            **self._solution
        )

    def fetch(self):
        """
        Fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.task_statistics.TaskStatisticsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.TaskStatisticsContext {}>".format(context)
