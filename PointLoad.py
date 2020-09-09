import numpy as np
import sys
from Point import *
# %% POINT LOAD
class pointLoad(point):
  # %% Properties
  value=np.array([float(0)])
  def check_value(self):
    check=True
    msg=[]
    if type(self.value)!=np.ndarray:
      check=False
      msg.append('pointLoad.value is not a ndarray (numpy)')
    else:
      aux=False
      for v in self.value:
        if type(v)!=np.float64:
          check=False
          aux=True
          print(type(v))
          pass
        pass
      if aux is True:
        msg.append('pointLoad.value components are not float')
        pass
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('pointLoad Checker')
      pass
    pass
  # %% Checker inherited
  # %% Constructor
  def __init__(self,point,value):
    if point is not None:
      super().__init__(point.x,point.y,point.z)
      pass
    value=value.astype(np.float64)
    self.value=value
    self.checker()
    pass
  # %% Methods
  # Method: Value
  def method():
    pass

  pass



