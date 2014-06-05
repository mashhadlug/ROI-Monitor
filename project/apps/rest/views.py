#-*- coding: utf-8 -*-
import re

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify
from flask.ext.babel import lazy_gettext as _

#project import
from project.apps.site.models import Sensor

mod = Blueprint('api', __name__, url_prefix='/api/v1')

@mod.route('/sensor/<id>')
def rest_sensor(id):
	sensor_obj = Sensor.query.filter(Sensor.id == id).first()
	# return sensor_obj.name
	print dir(sensor_obj)
	return jsonify(name = sensor_obj.name,
			id = sensor_obj.id,
			created_at = sensor_obj.created_at,
			created_by = sensor_obj.created_by,
			modified_at = sensor_obj.modified_at,
			modified_by = sensor_obj.modified_by,
			pin = sensor_obj.pin,
			)

@mod.route('/sensors/')
def rest_sensors():
	sensor_obj = Sensor.query.all()
	sensors = []
	for item in sensor_obj:
		tmp = {}
		tmp['name'] = item.name
		tmp['id'] = item.id
		tmp['created_at'] = item.created_at
		tmp['created_by'] = item.created_by
		tmp['modified_at'] = item.modified_at
		tmp['modified_by'] = item.modified_by
		tmp['pin'] = item.pin
		sensors.append(tmp)

	return jsonify(sensors=sensors)

