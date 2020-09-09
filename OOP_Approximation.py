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
# start (A) and end (B)
start_time = time.time()
for i in range(0,1):
  A=point(0,0,0)
  B=point(10,0,0)
  # line
  lineAB=line(A,B)
  # beam
  beamAB=beam(displacements=np.array([True,False,True]),rotations=np.array([False,True,False]),
              line=lineAB,
              boundaryBegin=np.array([True,True,False]),boundaryEnd=np.array([False,True,False]),
              report=True)
  # loads
  pointP=point(4,0,0)
  pointP2=point(2,0,0)
  P=pointLoad(pointP2,np.array([1,0,0]))
  P2=pointLoad(pointP,np.array([0,1,0]))
  P3=pointLoad(pointP,np.array([0,0,1]))

  beamAB.add_pointLoad(P,report=True)
  beamAB.add_pointLoad(P2,report=True)
  beamAB.add_pointLoad(P3,report=True)

  # print(beamAB.reactionBegin)
  # print(beamAB.reactionEnd)

  # i=0
  # for force in beamAB.forces:
  #   print(i)
  #   print(force.intervals)
  #   print(force.values)
  #   i+=1
  #   pass

  f=4
  force=beamAB.forces[f]
  print(force.intervals)
  print(force.values)
  # beamAB.plot_Forces()
  # force=beamAB.forces[f].get_integral()
  # print(force.intervals)
  # print(force.values)
  pass
print("--- %s seconds ---" % (time.time() - start_time))
