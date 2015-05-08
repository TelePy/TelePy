# -*- coding: utf-8 -*-

__author__, __date__ = 'mehdy', '5/4/15'

from telepy.base import RequestHandler


class RoomHandler(RequestHandler):

    __route__ = r'/room/([^/]*)'

    def get(self, slug):
        self.render('room.html')