# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Version
from twilio.rest.trunking.v1.trunk import TrunkList


class V1(Version):

    def __init__(self, domain):
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._trunks = None

    @property
    def trunks(self):
        if self._trunks is None:
            self._trunks = TrunkList(self)
        return self._trunks

    def __repr__(self):
        return '<Twilio.Trunking.V1>'
