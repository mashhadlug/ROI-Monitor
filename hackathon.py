#!/usr/bin/python

PINS = [dict(name="WC", file="/tmp/wc", pin="1")]

import threading
from  datetime  import datetime as dt
from project.apps.sensors.models import Log, Sensor
from project.database import db_session 
import time

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
    self.device = "/sys/class/gpio/gpio%s/value" % pin
    if not os.path.exists(self.device):
      f = open("/sys/class/gpio/exports")
      f.write(self.pin)
      f.close()
      time.sleep(2)
    print "Reading %s" % self.device
    
    self.current = 0
  
  def start_reading (self):
    """ Function doc """
    while True:
      f = open(self.device, "r")
      value = f.read()
      value = value.strip("\n")
      if value != self.current and value != "":
        print "id: %s from: %s to: %s", (self.sensor_id, self.current, value)
        log = Log(sensor_id=self.sensor_id, created_at=dt.now(), change_from=self.current, value=value)
        db_session.add(log)
        db_session.commit()
        self.current = value
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
  threads = []
  for item in sensor_obj:
    mon = Monitor(item.name, item.pin, item.id)
    threads.append(mon)
  for th in threads:  
    th.start()


if __name__ == "__main__":
  command_line_runner()
