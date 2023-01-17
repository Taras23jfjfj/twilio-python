"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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




class ExecutionContextContext(InstanceContext):
    def __init__(self, version: V2, flow_sid: str, execution_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid,  }
        self._uri = '/Flows/${flow_sid}/Executions/${execution_sid}/Context'
        
    
    def fetch(self):
        
        """
        Fetch the ExecutionContextInstance

        :returns: The fetched ExecutionContextInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sidexecution_sid=self._solution['flow_sid''execution_sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ExecutionContextContext>'



class ExecutionContextInstance(InstanceResource):
    def __init__(self, version, payload, flow_sid: str, execution_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'context' : payload.get('context'),
            'flow_sid' : payload.get('flow_sid'),
            'execution_sid' : payload.get('execution_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'flow_sid': flow_sid or self._properties['flow_sid']'execution_sid': execution_sid or self._properties['execution_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ExecutionContextContext(
                self._version,
                flow_sid=self._solution['flow_sid'],execution_sid=self._solution['execution_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.ExecutionContextInstance {}>'.format(context)



class ExecutionContextListInstance(ListResource):
    def __init__(self, version: V2, flow_sid: str, execution_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ExecutionContextListInstance>'

