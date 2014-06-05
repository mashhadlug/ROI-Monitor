#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify, render_template
from flask.ext.babel import lazy_gettext as _
from sqlalchemy import desc

#project import
from models import Sensor
from forms import SensorForm
from project.database import db_session

mod = Blueprint('sensors', __name__, url_prefix='/sensors')

@mod.route('/', methods=['GET'])
def index():
    sensor_form = SensorForm()
    sensors = Sensor.query.order_by(desc(Sensor.id)).all()
    return render_template("/sensors/index.html", form=sensor_form, sensors=sensors)

@mod.route('/', methods=['POST'])
def new():
    # TODO: add form vlidation 
    name = request.form.get('name', '')
    pin = request.form.get('pin', '')
    sensor = Sensor(name=name, pin=pin)
    db_session.add(sensor)
    db_session.commit()
    flash(u'successfully created new sensor', 'success')

    return redirect("/sensors/")

@mod.route('/<id>/', methods=['GET'])
def show(id):
    sensor = Sensor.query.filter(Sensor.id == id).first()
    return render_template("/sensors/sensor.html", sensor=sensor)

@mod.route('/<id>/', methods=['POST'])
def update(id):
    # TODO: check if sensor exists
    # TODO: add form vlidation
    sensor = Sensor.query.filter(Sensor.id == id).first()
    
    sensor.name = request.form.get('name', '')
    sensor.pin = request.form.get('pin', '')
    db_session.add(sensor)
    db_session.commit()
    flash(u'successfully updated the sensor', 'success')
    
    return redirect("/sensors")
