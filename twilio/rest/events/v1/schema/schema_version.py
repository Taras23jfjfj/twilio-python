"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page




class SchemaVersionContext(InstanceContext):
    def __init__(self, version: V1, id: str, schema_version: int):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'id': id, 'schema_version': schema_version,  }
        self._uri = '/Schemas/${id}/Versions/${schema_version}'
        
    
    def fetch(self):
        
        """
        Fetch the SchemaVersionInstance

        :returns: The fetched SchemaVersionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return SchemaVersionInstance(
            self._version,
            payload,
            idschema_version=self._solution['id''schema_version'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SchemaVersionContext>'



class SchemaVersionInstance(InstanceResource):
    def __init__(self, version, payload, id: str, schema_version: int):
        super().__init__(version)
        self._properties = { 
            'id' : payload.get('id'),
            'schema_version' : payload.get('schema_version'),
            'date_created' : payload.get('date_created'),
            'url' : payload.get('url'),
            'raw' : payload.get('raw'),
        }

        self._context = None
        self._solution = {
            'id': id or self._properties['id']'schema_version': schema_version or self._properties['schema_version']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SchemaVersionContext(
                self._version,
                id=self._solution['id'],schema_version=self._solution['schema_version'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.SchemaVersionInstance {}>'.format(context)



class SchemaVersionListInstance(ListResource):
    def __init__(self, version: V1, id: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'id': id,  }
        self._uri = '/Schemas/${id}/Versions'
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return SchemaVersionPage(self._version, payload, id=self._solution['id'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SchemaVersionListInstance>'

