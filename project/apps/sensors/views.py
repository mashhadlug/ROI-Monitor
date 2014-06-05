#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _

#project import
from models import Sensor
from project.database import db_session

mod = Blueprint('sensors', __name__, url_prefix='/sensors')

@mod.route('/')
def index():
    return render_template("/sensors/index.html")

@mod.route('/', methods=['POST'])
def new_sensor():
    name = request.form.get('name', '')
    pin = request.form.get('pin', '')
    sensor = Sensor(name=name, pin=pin)
    db_session.add(sensor)
    db_session.commit()
    return render_template("/sensors/index.html")

@mod.route('/test')
def index():
    return render_template("/sensors/index.html")

@mod.route('/sensor/<id>')
def rest_sensor(id):
    sensor_obj = Sensor.query.filter(Sensor.id == id).first()
    return sensor_obj.name

