#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _

#project import

mod = Blueprint('sensors', __name__, url_prefix='/sensors')

@mod.route('/')
def index():
    return render_template("/sensors/index.html")

@mod.route('/test')
def index():
    return render_template("/sensors/index.html")
