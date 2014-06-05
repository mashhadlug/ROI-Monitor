#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _

#project import
from models import Sensor
from forms import SensorForm
from project.database import db_session

mod = Blueprint('sensors', __name__, url_prefix='/sensors')

@mod.route('/')
def index():
    sensor_form = SensorForm()
    print sensor_form
    return render_template("/sensors/index.html", form=sensor_form)

@mod.route('/', methods=['POST'])
def new_sensor():
    name = request.form.get('name', '')
    pin = request.form.get('pin', '')
    sensor = Sensor(name=name, pin=pin)
    db_session.add(sensor)
    db_session.commit()
    return render_template("/sensors/index.html")

@mod.route('/sensor/<id>')
def rest_sensor(id):
    sensor_obj = Sensor.query.filter(Sensor.id == id).first()
    return render_template("/sensors/sensor.html", sensor=sensor_obj)
