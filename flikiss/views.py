#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Views for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'


import os.path as op
from werkzeug import secure_filename
from flask import (request, render_template, redirect, flash, url_for,
                   Blueprint, current_app, jsonify, send_from_directory)

from flikiss.forms import PageForm
from flikiss.models import Page
from flikiss.utils import render_markdown

# create blueprint
wiki = Blueprint('wiki', __name__)


@wiki.route('/')
def page(name) :
    """
        Render page
    """
    # get page
    page_name = request.args.get('page', current_app.config.get('START_PAGE'))
    page = Page(page_name, name)
    # get menu
    menu_name = current_app.config.get('MENU_PAGE')
    menu = Page(menu_name, name)
    return render_template('page.html', menu=menu, page=page, name=name)


@wiki.route('/_edit/', methods=['GET','POST'])
def edit(name) :
    """
        Edit page
    """
    # get page
    page_name = request.args.get('page', current_app.config.get('START_PAGE'))
    page = Page(page_name, name)
    # get menu
    menu_name = current_app.config.get('MENU_PAGE')
    menu = Page(menu_name, name)
    # fill form
    form = PageForm(content=page.content)
    if form.validate_on_submit() :
        # check password
        password = current_app.config.get('PASSWORD')
        if form.password.data == password :
            # save file
            page.content = form.content.data
            if page.content :
                flash('Page saved', 'info')
            else :
                flash('Page removed', 'info')
            return redirect(url_for('.page', page=page_name, name=name))
        else :
            flash('Invalid password', 'error')
    return render_template('edit.html', form=form, menu=menu, name=name)


@wiki.route('/_upload', methods=['POST'])
def upload(name) :
    """
        Upload images from edit page
    """
    # get file
    img = request.files['file']
    if img :
        # upload it
        filename = secure_filename(img.filename)
        path = current_app.config.get('UPLOAD_DIR', '.')
        img.save(op.join(path, filename))
        # contruct url
        url = url_for('.media', filename=filename)
        return jsonify(filename=url)
    return jsonify(error='Error while uploading the picture')


@wiki.route('/_media/<filename>')
def media(name, filename) :
    """
        Media files

        :param filename: File name
    """
    path = current_app.config.get('UPLOAD_DIR', '.')
    return send_from_directory(path, filename=filename)


@wiki.route('/_render', methods=['POST'])
def render(name) :
    """
        Render markdown
    """
    content = request.form.get('content','')
    return jsonify(value=render_markdown(content))
