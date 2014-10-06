#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    FliKISS 
    ~~~~~~~

    A personal wiki engine inspired from BlazeKISS
    based on flat files written in Markdown
"""

__author__ = u'TROUVERIE Joachim'

import os
import os.path as op
from flask import Flask
from flask.ext.codemirror import CodeMirror

from flikiss.views import wiki

def create_app(config=None) :
    """
        App factory
        
        :param config: Config file path
    """
    # create app
    app = Flask(__name__)
    # default config
    app.config.from_pyfile('config.py')
    # update config
    if config :
        app.config.from_object(config)
    # create path
    if not op.exists(app.config.get('PAGES_DIR')) :
        os.makedirs(app.config.get('PAGES_DIR'))
    if not op.exists(app.config.get('UPLOAD_DIR')) :
        os.makedirs(app.config.get('UPLOAD_DIR'))
    # extension
    codemirror = CodeMirror(app)
    # main blueprint
    app.register_blueprint(wiki, url_defaults={'name' : None})
    # blueprints
    bps = app.config.get('NAMESPACES', [])
    for bp in bps :
        app.register_blueprint(wiki, url_prefix='/{0}'.format(bp), 
                               url_defaults={'name' : bp})    
    return app

