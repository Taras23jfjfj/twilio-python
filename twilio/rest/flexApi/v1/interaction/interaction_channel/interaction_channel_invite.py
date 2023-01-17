"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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





class InteractionChannelInviteInstance(InstanceResource):
    def __init__(self, version, payload, interaction_sid: str, channel_sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'interaction_sid' : payload.get('interaction_sid'),
            'channel_sid' : payload.get('channel_sid'),
            'routing' : payload.get('routing'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'interaction_sid': interaction_sid or self._properties['interaction_sid']'channel_sid': channel_sid or self._properties['channel_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InteractionChannelInviteContext(
                self._version,
                interaction_sid=self._solution['interaction_sid'],channel_sid=self._solution['channel_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.InteractionChannelInviteInstance {}>'.format(context)



class InteractionChannelInviteListInstance(ListResource):
    def __init__(self, version: V1, interaction_sid: str, channel_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Interactions/${interaction_sid}/Channels/${channel_sid}/Invites'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return InteractionChannelInviteInstance(self._version, payload, interaction_sid=self._solution['interaction_sid']channel_sid=self._solution['channel_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return InteractionChannelInvitePage(self._version, payload, interaction_sid=self._solution['interaction_sid'], channel_sid=self._solution['channel_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.InteractionChannelInviteListInstance>'

