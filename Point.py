import numpy as np
import sys
# %% POINT
class point():
  # %% Properties
  x=None
  def check_x(self):
    check=True
    msg=[]
    if self.x is not None and type(self.x)!=float:
      check=False
      msg.append('point.x is not float')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('point Checker')
      pass
    pass
  y=None
  def check_y(self):
    check=True
    msg=[]
    if self.y is not None and type(self.y)!=float:
      check=False
      msg.append('point.y is not float')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('point Checker')
      pass
    pass
  z=None
  def check_z(self):
    check=True
    msg=[]
    if self.z is not None and type(self.z)!=float:
      check=False
      msg.append('point.z is not float')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('point Checker')
      pass
    pass
  # %% Checker
  def checker(self):
    [getattr(self, att)() for att in dir(self) if att.startswith('check') and not att.startswith('checker')and callable(getattr(self, att))]
    pass
  # %% Constructor
  def __init__(self,x=None,y=None,z=None):
    if x is not None:
      self.x=float(x)
      pass
    if y is not None:
      self.y=float(y)
      pass
    if z is not None:
      self.z=float(z)
      pass
    self.checker()
    pass
  # %% Methods
  # Method: Value
  def method():
    pass
  
  pass