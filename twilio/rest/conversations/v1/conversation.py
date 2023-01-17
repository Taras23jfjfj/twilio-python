"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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

from twilio.rest.conversation.message import MessageListInstancefrom twilio.rest.conversation.participant import ParticipantListInstancefrom twilio.rest.conversation.webhook import WebhookListInstance


class ConversationContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Conversations/${sid}'
        
        self._messages = None
        self._participants = None
        self._webhooks = None
    
    def delete(self, x_twilio_webhook_enabled):
        
        
        """
        Deletes the ConversationInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ConversationInstance

        :returns: The fetched ConversationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return ConversationInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )
        
        
    
    def update(self, x_twilio_webhook_enabled, body):
        data = values.of({
            'x_twilio_webhook_enabled': x_twilio_webhook_enabled,'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ConversationInstance(self._version, payload, sid=self._solution['sid'], )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConversationContext>'



class ConversationInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'messaging_service_sid' : payload.get('messaging_service_sid'),
            'sid' : payload.get('sid'),
            'friendly_name' : payload.get('friendly_name'),
            'unique_name' : payload.get('unique_name'),
            'attributes' : payload.get('attributes'),
            'state' : payload.get('state'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'timers' : payload.get('timers'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'bindings' : payload.get('bindings'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConversationContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def messages(self):
        return self._proxy.messages
    @property
    def participants(self):
        return self._proxy.participants
    @property
    def webhooks(self):
        return self._proxy.webhooks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConversationInstance {}>'.format(context)



class ConversationListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Conversations'
        
    
    def create(self, x_twilio_webhook_enabled, body):
        data = values.of({
            'x_twilio_webhook_enabled': x_twilio_webhook_enabled,'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return ConversationInstance(self._version, payload, )
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ConversationPage(self._version, payload, )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConversationListInstance>'

