#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify
from flask.ext.babel import lazy_gettext as _

#project import
from project.apps.site.models import Sensor

mod = Blueprint('api', __name__, url_prefix='/api')

@mod.route('/v1/sensor/<id>')
def rest_sensor(id):
	sensor_obj = Sensor.query.filter(Sensor.id == id).first()
	return sensor_obj.name
