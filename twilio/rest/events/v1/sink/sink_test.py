r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SinkTestInstance(InstanceResource):
    """
    :ivar result: Feedback indicating whether the test event was generated.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: str):
        super().__init__(version)

        self.result: Optional[str] = payload.get("result")

        self._solution = {
            "sid": sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.SinkTestInstance {}>".format(context)


class SinkTestList(ListResource):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SinkTestList

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies the Sink to be Tested.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Sinks/{sid}/Test".format(**self._solution)

    def create(self) -> SinkTestInstance:
        """
        Create the SinkTestInstance


        :returns: The created SinkTestInstance
        """

        payload = self._version.create(
            method="POST",
            uri=self._uri,
        )

        return SinkTestInstance(self._version, payload, sid=self._solution["sid"])

    async def create_async(self) -> SinkTestInstance:
        """
        Asynchronously create the SinkTestInstance


        :returns: The created SinkTestInstance
        """

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
        )

        return SinkTestInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.SinkTestList>"
