# -*- coding: utf-8 -*-

import inspect

from tornado.web import Application


def create_app(config):

    modules = __import__('telepy.handlers',
                         fromlist=list(config['active_handlers']))
    handlers = []
    for item in [getattr(modules, module) for module in
                 config['active_handlers']]:
        handlers.extend(
            [(handler.__route__, handler) for _, handler in
             inspect.getmembers(item, inspect.isclass)
             if handler.__module__.startswith('telepy.handlers')])

    app = Application(handlers=handlers, **config)
    return app