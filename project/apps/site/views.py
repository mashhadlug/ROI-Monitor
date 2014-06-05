#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify
from flask.ext.babel import lazy_gettext as _

#project import
from models import Sensor

mod = Blueprint('site', __name__, url_prefix='/')

@mod.route('/')
def index():
    return "Hello World <a href='/about/'> About </a>"

@mod.route('about/')
def about():
    """
    show Sensor
    """
    return "<center><h1>IRAN‌ PYTHON</h1></center>"

