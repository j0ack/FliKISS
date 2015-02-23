#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Login module for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

from functools import wraps

from flask import session, redirect, url_for, flash, request


def login_required(func):
    """
        Decorator to provide very simple
        auth control on views
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get('user'):
            flash('You must be logged in to access this page', 'info')
            return redirect(url_for('.login', next=request.url))
        else:
            return func(*args, **kwargs)
    return decorated_view


def login_user():
    """
        Log an admin user in session
    """
    session['user'] = 'Admin'


def logout_user():
    """
        Log out user
    """
    session['user'] = None
