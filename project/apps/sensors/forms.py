# from python
import re
import urllib

# from wtforms
from wtforms import IntegerField, TextField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import Required, Length, Regexp, Email, optional, EqualTo

# from flask
from flask import g
from flask.ext.wtf import Form
from flaskext.babel import lazy_gettext as _

# from friendfile
# from friendfile.models import Entity


class SensorForm(Form):
    name = TextField('Sensor\'s Name',
                            [Required(message='The name is required')])
    pin = TextField('Sensor\'s Pin Number',
                            [Required(message='a valid PIN number for the sensor is required')])
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
