"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
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




class CountryContext(InstanceContext):
    def __init__(self, version: V1, iso_country: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'iso_country': iso_country,  }
        self._uri = '/Voice/Countries/${iso_country}'
        
    
    def fetch(self):
        
        """
        Fetch the CountryInstance

        :returns: The fetched CountryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return CountryInstance(
            self._version,
            payload,
            iso_country=self._solution['iso_country'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CountryContext>'



class CountryInstance(InstanceResource):
    def __init__(self, version, payload, iso_country: str):
        super().__init__(version)
        self._properties = { 
            'country' : payload.get('country'),
            'iso_country' : payload.get('iso_country'),
            'outbound_prefix_prices' : payload.get('outbound_prefix_prices'),
            'inbound_call_prices' : payload.get('inbound_call_prices'),
            'price_unit' : payload.get('price_unit'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'iso_country': iso_country or self._properties['iso_country']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CountryContext(
                self._version,
                iso_country=self._solution['iso_country'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.CountryInstance {}>'.format(context)



class CountryListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Voice/Countries'
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return CountryPage(self._version, payload, )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CountryListInstance>'

