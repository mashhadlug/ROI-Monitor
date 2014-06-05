#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _

#project import

mod = Blueprint('site', __name__, url_prefix='/')

@mod.route('/')
def index():
    return render_template("dashboard.html")

@mod.route('about/')
def about():
    """
    show profile
    """
    return "<center><h1>IRAN‌ PYTHON</h1></center>"
