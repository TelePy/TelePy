#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__, __date__ = 'mehdy', '5/4/15'

import click
from tornado.ioloop import IOLoop

from telepy.app import create_app
from telepy.config import config


@click.group()
def main():
    """
    TelePy - Unified Messaging System
    """
    pass


@main.command()
@click.option('--host', '-h', default='', type=click.STRING,
              help='host address')
@click.option('--port', '-p', default=8080, help='port')
def run(host, port):
    """
    run the TelePy server
    """
    app = create_app(config)
    app.listen(port=port, address=host)
    app.logger.info("Started listening at 127.0.0.1:8080.")
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
