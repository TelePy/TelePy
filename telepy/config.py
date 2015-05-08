# -*- coding: utf-8 -*-

__author__, __date__ = 'mehdy', '5/4/15'

import os

rel = lambda *x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))

config = dict(template_path=rel('templates'),
              static_path=rel('static'),
              debug=True,
              active_handlers=(
                  'main',
                  'room',
                  'sockets'))