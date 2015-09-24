# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.api.v2010 import V2010
from twilio.rest.base import Domain


class Api(Domain):

    def __init__(self, twilio):
        super(Api, self).__init__(twilio)
        self.base_url = 'https://api.twilio.com'
        self._v2010 = None

    @property
    def v2010(self):
        if self._v2010 is None:
            self._v2010 = V2010(self)
        return self._v2010

    def __repr__(self):
        return '<Twilio.Api>'
