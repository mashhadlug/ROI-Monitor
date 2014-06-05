#-*- coding: utf-8 -*-
import re
import json

# flask import
from flask import Blueprint, abort, request, current_app, flash, session, g, redirect, url_for, send_from_directory, make_response, jsonify

#project import
from project.apps.sensors.models import Sensor, Log
from sqlalchemy import desc

mod = Blueprint('api', __name__, url_prefix='/api/v1')

@mod.route('/sensor/<id>')
def rest_sensor(id):
	sensor_obj = Sensor.query.filter(Sensor.id == id).first()
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

	return json.dumps(sensors)

@mod.route('/sensor/log/<id>')
@mod.route('/sensor/log/', defaults={'id': '0'})
def rest_senser_log(id):
	if int(id) == 0 :
		sensor_obj = Sensor.query.all()
		# log_obj = Log.query.all()
	else:
		sensor_obj = [Sensor.query.filter(Sensor.id == id).first()]
		print (sensor_obj)
		# log_obj = Log.query.filter(Log.sensor_id == id)

	result = []
	for sensor in sensor_obj:
		res = {}
		log_obj = Log.query.filter(Log.sensor_id == sensor.id)
		res['name'] = sensor.name
		res['id'] = sensor.id
		res['created_at'] = sensor.created_at
		res['created_by'] = sensor.created_by
		res['modified_at'] = sensor.modified_at
		res['modified_by'] = sensor.modified_by
		res['pin'] = sensor.pin
		logs = []
		for item in log_obj:
			tmp = {}
			tmp['id'] = item.sensor_id
			tmp['created_at'] = item.created_at
			tmp['change_from'] = item.change_from
			tmp['value'] = item.value
			logs.append(tmp)
		res['log'] = logs
		result.append(res)

	return json.dumps(result)

@mod.route('/sensor/status/<id>')
def rest_status(id):
	sensor_obj = Log.query.filter(Log.sensor_id == id).order_by(desc(Log.created_at)).first()
	return jsonify(value=sensor_obj.value)
