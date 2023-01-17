"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page




class AssignedAddOnExtensionContext(InstanceContext):
    def __init__(self, version: V2010, account_sid: str, resource_sid: str, assigned_add_on_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'resource_sid': resource_sid, 'assigned_add_on_sid': assigned_add_on_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/IncomingPhoneNumbers/${resource_sid}/AssignedAddOns/${assigned_add_on_sid}/Extensions/${sid}.json'
        
    
    def fetch(self):
        
        """
        Fetch the AssignedAddOnExtensionInstance

        :returns: The fetched AssignedAddOnExtensionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return AssignedAddOnExtensionInstance(
            self._version,
            payload,
            account_sidresource_sidassigned_add_on_sidsid=self._solution['account_sid''resource_sid''assigned_add_on_sid''sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnExtensionContext>'



class AssignedAddOnExtensionInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, resource_sid: str, assigned_add_on_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'resource_sid' : payload.get('resource_sid'),
            'assigned_add_on_sid' : payload.get('assigned_add_on_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'product_name' : payload.get('product_name'),
            'unique_name' : payload.get('unique_name'),
            'uri' : payload.get('uri'),
            'enabled' : payload.get('enabled'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid']'resource_sid': resource_sid or self._properties['resource_sid']'assigned_add_on_sid': assigned_add_on_sid or self._properties['assigned_add_on_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AssignedAddOnExtensionContext(
                self._version,
                account_sid=self._solution['account_sid'],resource_sid=self._solution['resource_sid'],assigned_add_on_sid=self._solution['assigned_add_on_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AssignedAddOnExtensionInstance {}>'.format(context)



class AssignedAddOnExtensionListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str, resource_sid: str, assigned_add_on_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'resource_sid': resource_sid, 'assigned_add_on_sid': assigned_add_on_sid,  }
        self._uri = '/Accounts/${account_sid}/IncomingPhoneNumbers/${resource_sid}/AssignedAddOns/${assigned_add_on_sid}/Extensions.json'
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AssignedAddOnExtensionPage(self._version, payload, account_sid=self._solution['account_sid'], resource_sid=self._solution['resource_sid'], assigned_add_on_sid=self._solution['assigned_add_on_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnExtensionListInstance>'

