#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Launcher for FliKISS app
"""

__author__ = u'TROUVERIE Joachim'

import os.path as op
from argparse import ArgumentParser
from cherrypy import wsgiserver

from flikiss import create_app

def run() :
    """
        Main launcher for FliKISS

        :param ip: Host to serve the app
        :param port: Port to serve tha app
        :param url: Url to serve the app
        :param debug: Debug mode
        :param config: Path to alternative config file
    """
    # create args parser
    parser = ArgumentParser(description=__doc__)
    # add arguments
    parser.add_argument('-i','--ip',help='Host to serve the app',default='127.0.0.1')
    parser.add_argument('-p','--port',help='Port to serve the app',default=8000,type=int)
    parser.add_argument('-u','--url',help='Url to serve the app',default='/')
    parser.add_argument('-d','--debug',action='store_true',help='Debug mode')
    parser.add_argument('-c','--config',help='Alternate config file',default=None)
    # parse given args
    args = parser.parse_args()
    # config management
    if args.config :
        app = create_app(args.config)
    else :
        # default config
        config_path = op.expanduser('~/.flikissrc')
        if op.exists(config_path) :
            app = create_app(config_path)
        else :
            app = create_app()
    # debug mode
    if args.debug :
        app.debug = True
        app.run(port=args.port)
    else :
        # create server
        d = wsgiserver.WSGIPathInfoDispatcher({args.url: app.wsgi_app})
        server = wsgiserver.CherryPyWSGIServer((args.ip, args.port), d)
        print 'App served on {0}:{1}'.format(args.ip, args.port)
        server.start()
    
    
if __name__ == '__main__' :
    run()
