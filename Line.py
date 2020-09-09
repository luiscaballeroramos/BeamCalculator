import numpy as np
import sys
from Point import *
from PointLoad import *
# %% LINE
class line():
  # %% Properties
  begin=None
  def check_begin(self):
    check=True
    msg=[]
    if self.begin is not None and type(self.begin)!=point:
      check=False
      msg.append('line.begin is not a point object')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('line Checker')
      pass
    pass
  end=None
  def check_end(self):
    check=True
    msg=[]
    if self.end is not None and type(self.end)!=point:
      check=False
      msg.append('line.end is not a point object')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('line Checker')
      pass
    pass
  l=None
  # %% Checker
  def checker(self):
    [getattr(self, att)() for att in dir(self) if att.startswith('check') and not att.startswith('checker')and callable(getattr(self, att))]
    pass
  # %% Constructor
  def __init__(self,begin=None,end=None):
    self.begin=begin
    self.end=end
    self.l=self.get_L()
    self.checker()
    pass
  # %% Methods
  # Method: Length
  def get_L(self,point1=None,point2=None):
    if point1==None and point2==None:
      point1=self.begin
      point2=self.end
      pass
    if type(point1) in [point,pointLoad] and type(point2) in [point,pointLoad]:
      return ((point2.x-point1.x)**2+(point2.y-point1.y)**2+(point2.z-point1.z)**2)**(1/2)
    pass

  pass