# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AuthorizedConnectAppList(ListResource):

    def __init__(self, version, account_sid):
        super(AuthorizedConnectAppList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/AuthorizedConnectApps.json".format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._version.read(
            self,
            AuthorizedConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AuthorizedConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        return AuthorizedConnectAppContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Api.V2010.AuthorizedConnectAppList>'


class AuthorizedConnectAppContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(AuthorizedConnectAppContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/AuthorizedConnectApps/{sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AuthorizedConnectAppInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )


class AuthorizedConnectAppInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(AuthorizedConnectAppInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'connect_app_company_name': payload['connect_app_company_name'],
            'connect_app_description': payload['connect_app_description'],
            'connect_app_friendly_name': payload['connect_app_friendly_name'],
            'connect_app_homepage_url': payload['connect_app_homepage_url'],
            'connect_app_sid': payload['connect_app_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'permissions': payload['permissions'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = AuthorizedConnectAppContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def connect_app_company_name(self):
        """ The connect_app_company_name """
        return self._properties['connect_app_company_name']

    @property
    def connect_app_description(self):
        """ The connect_app_description """
        return self._properties['connect_app_description']

    @property
    def connect_app_friendly_name(self):
        """ The connect_app_friendly_name """
        return self._properties['connect_app_friendly_name']

    @property
    def connect_app_homepage_url(self):
        """ The connect_app_homepage_url """
        return self._properties['connect_app_homepage_url']

    @property
    def connect_app_sid(self):
        """ The connect_app_sid """
        return self._properties['connect_app_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def permissions(self):
        """ The permissions """
        return self._properties['permissions']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()
