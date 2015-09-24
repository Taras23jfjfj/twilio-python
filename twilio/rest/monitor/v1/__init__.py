# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Version
from twilio.rest.monitor.v1.alert import AlertList
from twilio.rest.monitor.v1.event import EventList


class V1(Version):

    def __init__(self, domain):
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._alerts = None
        self._events = None

    @property
    def alerts(self):
        if self._alerts is None:
            self._alerts = AlertList(self)
        return self._alerts

    @property
    def events(self):
        if self._events is None:
            self._events = EventList(self)
        return self._events

    def __repr__(self):
        return '<Twilio.Monitor.V1>'
