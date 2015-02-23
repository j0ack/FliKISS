#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Forms for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

from wtforms import PasswordField, TextAreaField
from flask.ext.wtf import Form


class PageForm(Form):

    """
        Page form
    """
    markdown_content = TextAreaField('Content')


class LoginForm(Form):

    """
        Login form
    """
    password = PasswordField('Password')
