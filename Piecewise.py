import numpy as np

class piecewiseFunction():
  # Properties
  intervals={}
  values={}
  # Constructor
  def __init__(self,intervals=None,values=None,report=False):
    self.intervals={}
    self.values={}
    self.add_pieces(intervals,values,report=report)
    pass
  # Method: add pieces
  def add_pieces(self,intervals=None,values=None,report=False):
    # %% Check intervals and values
    check_intervals=True
    # check intervals
    if type(intervals)==list:
      for interval in intervals:
        if type(interval)==list:
          if len(interval)==2:
            pass
          else:
            check_intervals=False
            pass
        else:
          check_intervals=False
          pass
        pass
      pass
    else:
      check_intervals=False
      pass
    # check values
    check_values=True
    if check_intervals is True:
      if type(values)==list:
        for value in values:
          if type(value)==np.poly1d:
            pass
          else:
            check_values=False
            pass
          pass
        pass
      else:
        check_values=False
        pass
      pass
    # %% Interval assign
    if check_intervals is True and check_values is True:
      # for each interval to add
      for interval2,value2 in zip(intervals,values):
        # first interval
        if len(self.intervals)==0:
          self.intervals[len(self.intervals)+1]=interval2
          self.values[len(self.values)+1]=value2
          print('first interval and value in piecewise')
          pass
        # not first interval
        else:
          independent=True
          # for each existing interval
          for i in range(len(self.intervals)):
            if independent:
              interval1=self.intervals[i+1]
              value1=self.values[i+1]
              # relative position of interval2 from interval1
              begin=0
              if interval2[0]<interval1[0]:
                begin=1
              elif interval2[0]==interval1[0]:
                begin=2
              elif interval2[0]>interval1[0] and interval2[0]<interval1[1]:
                begin=3
              elif interval2[0]==interval1[1]:
                begin=4
              elif interval2[0]>interval1[1]:
                begin=5
                pass
              end=0
              if interval2[1]<interval1[0]:
                end=1
              elif interval2[1]==interval1[0]:
                end=2
              elif interval2[1]>interval1[0] and interval2[1]<interval1[1]:
                end=3
              elif interval2[1]==interval1[1]:
                end=4
              elif interval2[1]>interval1[1]:
                end=5
                pass
              # operations
              if begin==1:
                if end==1:
                  # independent
                  #      ----
                  # ----
                  pass
                elif end==2:
                  # independent
                  #     ----
                  # ----
                  pass
                elif end==3:
                  independent=False
                  #   ----
                  # ----
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.intervals[i+1]=[interval2[1],interval1[1]]
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval1[0]],[interval1[0],interval2[1]]],values=[value2,value1+value2],report=report)
                  pass
                elif end==4:
                  independent=False
                  #   ----
                  # ------
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.values[i+1]=value1+value2
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval1[0]]],values=[value2],report=report)
                  pass
                elif end==5:
                  independent=False
                  #   ----
                  # --------
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.values[i+1]=value1+value2
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval1[0]],[interval1[1],interval2[1]]],values=[value2,value2],report=report)
                  pass
              elif begin==2:
                if end==3:
                  independent=False
                  # ----
                  # --
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.intervals[i+1]=[interval2[1],interval1[1]]
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval2[1]]],values=[value1+value2],report=report)
                  pass
                elif end==4:
                  independent=False
                  # ----
                  # ----
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.values[i+1]=value1+value2
                  pass
                elif end==5:
                  independent=False
                  # ----
                  # ------
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.values[i+1]=value1+value2
                  # add new intervals
                  self.add_pieces(intervals=[[interval1[1],interval2[1]]],values=[value2],report=report)
                  pass
              elif begin==3:
                if end==3:
                  independent=False
                  # ----
                  #  --
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.intervals[i+1]=[interval1[0],interval2[0]]
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval2[1]],[interval2[1],interval1[1]]],values=[value1+value2,value1],report=report)
                  pass
                elif end==4:
                  independent=False
                  # ----
                  #   --
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.intervals[i+1]=[interval1[0],interval2[0]]
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval2[1]]],values=[value1+value2],report=report)
                  pass
                elif end==5:
                  independent=False
                  # ----
                  #   ----
                  if report: print(begin,end,interval1,interval2)
                  # replace interval1
                  self.intervals[i+1]=[interval1[0],interval2[0]]
                  # add new intervals
                  self.add_pieces(intervals=[[interval2[0],interval1[1]],[interval1[1],interval2[1]]],values=[value1+value2,value1+value2],report=report)
                  pass
              elif begin==4:
                if end==5:
                  # independent
                  # ----
                  #     ----
                  pass
              elif begin==5:
                if end==5:
                  # independent
                  # ----
                  #      ----
                  pass
                pass
              pass
            pass
          if independent is True:
            if report: print('independent',self.intervals,interval2)
            self.intervals[len(self.intervals)+1]=interval2
            self.values[len(self.values)+1]=value2
            pass
          pass
        pass
      pass
    pass
  # Method: get polynomial in a point
  def get_poly(self,x):
    poly=np.poly1d([0])
    for i in range(len(self.intervals)):
      interval=self.intervals[i+1]
      value=self.values[i+1]
      if x>=interval[0] and x<interval[1]:
        poly+=value
        pass
      pass
    return poly
  # Method: get value in a point
  def get_value(self,x):
    poly=self.get_poly(x)
    return poly(x)
  def get_integral(self):
    partial=0
    for i in range(0,len(self.intervals)):
      interval=self.intervals[i+1]
      value=self.values[i+1]
      if i==0:
        integral=piecewiseFunction([interval],[value.integ()])
        pass
      else:
        integral.add_pieces([interval],[value.integ()])
        pass
      pass
    return integral

  pass