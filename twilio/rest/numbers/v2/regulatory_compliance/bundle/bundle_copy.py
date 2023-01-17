"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
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





class BundleCopyInstance(InstanceResource):
    def __init__(self, version, payload, bundle_sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'regulation_sid' : payload.get('regulation_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'status' : payload.get('status'),
            'valid_until' : payload.get('valid_until'),
            'email' : payload.get('email'),
            'status_callback' : payload.get('status_callback'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
        }

        self._context = None
        self._solution = {
            'bundle_sid': bundle_sid or self._properties['bundle_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = BundleCopyContext(
                self._version,
                bundle_sid=self._solution['bundle_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.BundleCopyInstance {}>'.format(context)



class BundleCopyListInstance(ListResource):
    def __init__(self, version: V2, bundle_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'bundle_sid': bundle_sid,  }
        self._uri = '/RegulatoryCompliance/Bundles/${bundle_sid}/Copies'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return BundleCopyInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return BundleCopyPage(self._version, payload, bundle_sid=self._solution['bundle_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.BundleCopyListInstance>'

