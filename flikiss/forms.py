#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Forms for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

from wtforms import PasswordField
from flask.ext.codemirror.fields import CodeMirrorField
from flask.ext.wtf import Form

class PageForm(Form) :
    """
        Page form
    """
    password = PasswordField('Password')
    content = CodeMirrorField(language='markdown',
                                config = {'lineWrapping' : 'true' },
                                label = 'Content')

