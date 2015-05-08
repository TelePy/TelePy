# -*- coding: utf-8 -*-

import inspect
import logging
import sys

from tornado.web import Application


def create_app(config):
    """
    create the application
    :param config:
    :return:
    """
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
    app.logger = get_logger()
    return app


def get_logger():
    """
    create logger for application
    :return:
    """
    formatter = logging.Formatter(
        '-' * 40 + '\n%(asctime)s %(levelname)s [%(module)s.%(funcName)s: %('
                   'lineno)d]: %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger