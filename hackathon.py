#!/usr/bin/python

PINS = [dict(name="WC", file="/tmp/wc", pin="1")]

import threading
import datetime.datetime as dt
from project.apps.sensors.models import Log, Sensor

class Monitor(threading.Thread):
  """ Class doc """
  
  def __init__ (self, name=None, pin=None, sensor_id=None):
    """ Class initialiser """
    threading.Thread.__init__(self)
    
    if name is None or pin is None or sensor_id is None:
      raise Exception("ValueError", "name and pin number is essenial")
    
    if not isinstance(pin, int):
      raise Exception("ValueError", "pin number ust be a number")

    if not isinstance(sensor_id, int):
      raise Exception("ValueError", "Sensor Is is not valid")
    
    self.name = name
    self.pin = pin
    self.sensor_id = sensor_id
    self.device = "/tmp/%s" % pin
    self.current = None
  
  def start_reading (self):
    """ Function doc """
    while True:
      f = open(self.device, "r")
      value = f.read()
      if value != self.current:
        log = Log(sensor_id=self.sensor_id, created_at=dt.now(), change_from=value, value=self.current)
        db_session.add(log)
        db_session.commit()
        self.current = value
        print "Changed:",  value
        f.close()
  
  def run (self):
    """ Function doc """
    self.start_reading()
    pass

class Event:
  """ Class doc """
  
  def __init__ (self):
    """ Class initialiser """
    pass

def command_line_runner():
  sensor_obj = Sensor.query.all()
  for item in sensor_obj:
    mon = Monitor(item.name, item.pin, item.id)
  mon.start()


if __name__ == "__main__":
  command_line_runner()
