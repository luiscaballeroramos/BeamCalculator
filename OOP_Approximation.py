import numpy as np
import sys
import time

sys.path.append('D:/403_InProgressPROJECTS/2007_BeamCalculator/200804_OOPApproximation')
from Point import *
from Line import *
from Beam import *

from PointLoad import *
# %% clear console
print(chr(27) + "[2J")
#  set console report options
report=True
# start (A) and end (B)
start_time = time.time()
for i in range(0,1):
  A=point(0,0,0)
  B=point(10,0,0)
  # line
  lineAB=line(A,B)
  # beam
  beamAB=beam(translations=np.array([True,False,True]),rotations=np.array([False,True,False]),
              line=lineAB,
              boundaryBegin=np.array([True,True,False]),boundaryEnd=np.array([False,True,False]),
              report=report)
  # loads
  pointP=point(4,0,0)
  pointP2=point(2,0,0)
  P=pointLoad(pointP2,np.array([1,0,0]))
  P2=pointLoad(pointP,np.array([0,1,0]))
  P3=pointLoad(pointP,np.array([0,0,1]))

  beamAB.add_pointLoad(P,report=report)
  beamAB.add_pointLoad(P2,report=report)
  # beamAB.add_pointLoad(P3,report=report)

  beamAB.calculate(report)
  # print(beamAB.reactionBegin)
  # print(beamAB.reactionEnd)

  # i=0
  # for force in beamAB.forces:
  #   print('_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:')
  #   print(i)
  #   force.print()
  #   i+=1
  #   pass

  f=4
  # force=beamAB.forces[f]
  # force.print()
  beamAB.plot_Forces()
  # print('integral')
  # force=beamAB.forces[f].get_integral()
  # force.print()
  pass
print("--- %s seconds ---" % (time.time() - start_time))
