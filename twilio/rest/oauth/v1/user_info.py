"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
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




class UserInfoContext(InstanceContext):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/userinfo'
        
    
    def fetch(self):
        
        """
        Fetch the UserInfoInstance

        :returns: The fetched UserInfoInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return UserInfoInstance(
            self._version,
            payload,
            =self._solution[],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.UserInfoContext>'



class UserInfoInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'user_sid' : payload.get('user_sid'),
            'first_name' : payload.get('first_name'),
            'last_name' : payload.get('last_name'),
            'friendly_name' : payload.get('friendly_name'),
            'email' : payload.get('email'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = UserInfoContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.UserInfoInstance {}>'.format(context)



class UserInfoListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.UserInfoListInstance>'

