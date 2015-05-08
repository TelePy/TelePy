# -*- coding: utf-8 -*-

__author__, __date__ = 'mehdy', '5/4/15'


class Room(object):
    def __init__(self, name, clients=None):
        self.name = name
        self.clients = clients or []

    def __repr__(self):
        return "<Room #{}>".format(self.name)