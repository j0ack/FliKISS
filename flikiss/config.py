#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Default config for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

import os.path as op
from uuid import uuid4

PASSWORD = 'password'
SECRET_KEY = uuid4().hex
CODEMIRROR_LANGUAGES = ['markdown']
CODEMIRROR_THEME = 'xq-light'
PAGES_DIR = op.join(op.dirname(__file__), 'pages')
UPLOAD_DIR = op.join(op.dirname(__file__), 'media')
START_PAGE = 'index'
MENU_PAGE = 'menu'
FILE_EXTENSION = '.md'
NAMESPACES= []
