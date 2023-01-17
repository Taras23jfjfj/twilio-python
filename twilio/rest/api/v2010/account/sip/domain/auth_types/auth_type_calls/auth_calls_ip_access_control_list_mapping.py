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




class AuthCallsIpAccessControlListMappingContext(InstanceContext):
    def __init__(self, version: V2010, account_sid: str, domain_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${domain_sid}/Auth/Calls/IpAccessControlListMappings/${sid}.json'
        
    
    def delete(self):
        
        
        """
        Deletes the AuthCallsIpAccessControlListMappingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the AuthCallsIpAccessControlListMappingInstance

        :returns: The fetched AuthCallsIpAccessControlListMappingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return AuthCallsIpAccessControlListMappingInstance(
            self._version,
            payload,
            account_siddomain_sidsid=self._solution['account_sid''domain_sid''sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthCallsIpAccessControlListMappingContext>'



class AuthCallsIpAccessControlListMappingInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, domain_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'sid' : payload.get('sid'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid']'domain_sid': domain_sid or self._properties['domain_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AuthCallsIpAccessControlListMappingContext(
                self._version,
                account_sid=self._solution['account_sid'],domain_sid=self._solution['domain_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AuthCallsIpAccessControlListMappingInstance {}>'.format(context)



class AuthCallsIpAccessControlListMappingListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str, domain_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${domain_sid}/Auth/Calls/IpAccessControlListMappings.json'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return AuthCallsIpAccessControlListMappingInstance(self._version, payload, account_sid=self._solution['account_sid']domain_sid=self._solution['domain_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AuthCallsIpAccessControlListMappingPage(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthCallsIpAccessControlListMappingListInstance>'

