# -*- coding: utf-8 -*-

__author__, __date__ = 'mehdy', '5/4/15'

from telepy.base import RequestHandler
import uuid


class MainHandler(RequestHandler):

    __route__ = r'/'

    def get(self):
        room = str(uuid.uuid4().get_hex().upper()[0:6])
        self.redirect('/room/' + room)
