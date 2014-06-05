#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _
from sqlalchemy import desc


#project import
from project.apps.sensors.models import Sensor

mod = Blueprint('site', __name__, url_prefix='/')

@mod.route('/')
def index():
    sensors = Sensor.query.order_by(desc(Sensor.id)).all()
    return render_template("dashboard.html", sensors=sensors)

@mod.route('about/')
def about():
    """
    show Sensor
    """
    return "<center><h1>IRAN‌ PYTHON</h1></center>"
