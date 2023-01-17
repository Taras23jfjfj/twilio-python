"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource




class WorkflowStatisticsContext(InstanceContext):
    def __init__(self, version: V1, workspace_sid: str, workflow_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workflows/${workflow_sid}/Statistics'
        
    
    def fetch(self, minutes, start_date, end_date, task_channel, split_by_wait_time):
        
        """
        Fetch the WorkflowStatisticsInstance

        :returns: The fetched WorkflowStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return WorkflowStatisticsInstance(
            self._version,
            payload,
            workspace_sidworkflow_sid=self._solution['workspace_sid''workflow_sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkflowStatisticsContext>'



class WorkflowStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, workflow_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'cumulative' : payload.get('cumulative'),
            'realtime' : payload.get('realtime'),
            'workflow_sid' : payload.get('workflow_sid'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid']'workflow_sid': workflow_sid or self._properties['workflow_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkflowStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],workflow_sid=self._solution['workflow_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.WorkflowStatisticsInstance {}>'.format(context)



class WorkflowStatisticsListInstance(ListResource):
    def __init__(self, version: V1, workspace_sid: str, workflow_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkflowStatisticsListInstance>'

