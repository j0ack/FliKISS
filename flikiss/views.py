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

from flikiss.forms import PageForm, LoginForm
from flikiss.models import Page
from flikiss.utils import render_markdown
from flikiss.login import login_required, login_user, logout_user

# create blueprint
wiki = Blueprint('wiki', __name__)


@wiki.route('/')
def page(name):
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


@wiki.route('/_edit/', methods=['GET', 'POST'])
@login_required
def edit(name):
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
    form = PageForm(markdown_content=page.content)
    if form.validate_on_submit():
        # save file
        page.content = form.markdown_content.data
        if page.content:
            flash('Page saved', 'info')
        else:
            flash('Page removed', 'info')
        return redirect(url_for('.page', page=page_name, name=name))
    return render_template('edit.html', form=form, menu=menu, name=name)


@wiki.route('/_login/', methods=['GET', 'POST'])
def login(name):
    """
        Login view
    """
    menu_name = current_app.config.get('MENU_PAGE')
    menu = Page(menu_name, name)
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        if password == current_app.config.get('PASSWORD'):
            login_user()
            return redirect(request.args.get('next') or url_for('.page'))
        else:
            flash('Invalid password', 'error')
    return render_template('login.html', form=form, menu=menu)


def logout():
    """
        Logout user
    """
    logout_user()
    return redirect('/')


@login_required
def upload():
    """
        Upload images from edit page
    """
    # get file
    img = request.files['file']
    if img:
        # upload it
        filename = secure_filename(img.filename)
        path = current_app.config.get('UPLOAD_DIR', '.')
        img.save(op.join(path, filename))
        # contruct url
        url = url_for('media', filename=filename)
        return jsonify(url=url, name=filename)
    return jsonify(error='Error while uploading the picture')


def media(filename):
    """
        Media files

       :param filename: File name
    """
    path = current_app.config.get('UPLOAD_DIR', '.')
    return send_from_directory(path, filename=filename)


def render():
    """
        Render markdown
    """
    content = request.form.get('content', '')
    return jsonify(value=render_markdown(content))
