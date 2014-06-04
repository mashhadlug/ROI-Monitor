#!/usr/bin/python

PINS = [dict(name="WC", file="/tmp/wc", pin="1")]

import threading

class Monitor(threading.Thread):
  """ Class doc """
  
  def __init__ (self, name=None, pin=None):
    """ Class initialiser """
    threading.Thread.__init__(self)
    
    if name is None or pin is None:
      raise Exception("ValueError", "name and pin number is essenial")
    
    if not isinstance(pin, int):
      raise Exception("ValueError", "pin number ust be a number")
    
    self.name = name
    self.pin = pin
    self.device = "/tmp/%s" % pin
    self.current = None
  
  def start_reading (self):
    """ Function doc """
    while True:
      f = open(self.device, "r")
      value = f.read()
      if value != self.current:
        # TODO: trigger specific event
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
  mon = Monitor("WC", 1)
  mon.start()


if __name__ == "__main__":
  command_line_runner()
