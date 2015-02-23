#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Models for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

import os
import re
import os.path as op
from lockfile import LockFile as lock
from flask import current_app

from flikiss.utils import render_markdown


class Page(object):

    """
        Page object

       :param name: Page name
       :param prefix: Page path prefix
    """

    def __init__(self, name, prefix=None):
        self.name = self._slugify(name)
        self.prefix = prefix

    @classmethod
    def _slugify(cls, name):
        """
            Slugify name

           :param name: Page name
        """
        # remove special chars
        value = re.sub(r'[^\w\s-]', '', name).strip().lower()
        # remove spaces
        return re.sub(r'[-\s]+', '-', value)

    @property
    def path(self):
        """
            Page absolute path
        """
        # get root dir
        dirpath = current_app.config.get('PAGES_DIR')
        # get files extension from config
        ext = current_app.config.get('FILE_EXTENSION')
        # add prefix to path if exists
        if self.prefix:
            return op.join(dirpath, self.prefix, self.name + ext)
        else:
            return op.join(dirpath, self.name + ext)

    @property
    def content(self):
        """
            Page content or None if file does not exists
        """
        if not op.exists(self.path):
            return None
        # lock file to prevent concurrent access
        with lock(self.path):
            return open(self.path).read().decode('utf-8')

    @content.setter
    def content(self, value):
        """
            Save or remove object

           :param value: New content if `None` or empty then file is removed
        """
        # delete page
        if not value:
            if op.exists(self.path):
                os.remove(self.path)
        # save content
        else:
            # get path
            dirname = op.dirname(self.path)
            # create path if not exists
            if not op.exists(dirname):
                os.makedirs(dirname)
            # lock file to prevent concurrent access
            with lock(self.path):
                with open(self.path, 'wb') as page:
                    page.write(value.encode('utf-8'))

    @property
    def html(self):
        """
            Html repr if file exists or None
        """
        # check if file exists
        if not self.content:
            return None
        # translate Markdown to HTML
        return render_markdown(self.content)
