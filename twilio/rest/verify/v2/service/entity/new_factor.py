"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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





class NewFactorInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, identity: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'entity_sid' : payload.get('entity_sid'),
            'identity' : payload.get('identity'),
            'binding' : payload.get('binding'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'status' : payload.get('status'),
            'factor_type' : payload.get('factor_type'),
            'config' : payload.get('config'),
            'metadata' : payload.get('metadata'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'identity': identity or self._properties['identity']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NewFactorContext(
                self._version,
                service_sid=self._solution['service_sid'],identity=self._solution['identity'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.NewFactorInstance {}>'.format(context)



class NewFactorListInstance(ListResource):
    def __init__(self, version: V2, service_sid: str, identity: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity,  }
        self._uri = '/Services/${service_sid}/Entities/${identity}/Factors'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return NewFactorInstance(self._version, payload, service_sid=self._solution['service_sid']identity=self._solution['identity'])
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.NewFactorListInstance>'

