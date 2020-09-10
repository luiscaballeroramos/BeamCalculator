import matplotlib.pyplot as plt
import numpy as np
import sys
from Point import *
from Line import *
from PointLoad import *
from Piecewise import *
# %% BEAM
class beam(line):
  # %% Properties
  # begin=None
  # end=None
  dof=int(6)
  def check_dof(self):
    check=True
    msg=[]
    if type(self.dof)!=int:
      check=False
      msg.append('beam.dof is not an int')
    elif self.dof<1 or self.dof>6:
      check=False
      msg.append('beam.dof is not a number between 1 and 6')
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('beam Checker')
      pass
    pass
  translations=np.zeros(3,dtype=bool)
  def check_translations(self):
    check=True
    msg=[]
    if type(self.translations)!=np.ndarray:
      check=False
      msg.append('beam.translations is not a ndarray (numpy)')
    else:
      aux=False
      for d in self.translations:
        if type(d)!=np.bool_:
          check=False
          aux=True
          pass
        pass
      if aux is True:
        msg.append('beam.translations components are not bool')
        pass
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('beam Checker')
      pass
    pass
  rotations=np.zeros(3,dtype=bool)
  def check_rotations(self):
    check=True
    msg=[]
    if type(self.rotations)!=np.ndarray:
      check=False
      msg.append('beam.rotations is not a ndarray (numpy)')
    else:
      aux=False
      for r in self.rotations:
        if type(r)!=np.bool_:
          check=False
          aux=True
          pass
        pass
      if aux is True:
        msg.append('beam.rotations components are not bool')
        pass
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('beam Checker')
      pass
    pass
  boundaryBegin=np.zeros(6,dtype=bool)
  def check_boundaryBegin(self):
    check=True
    msg=[]
    if type(self.boundaryBegin)!=np.ndarray:
      check=False
      msg.append('beam.boundaryBegin is not a ndarray (numpy)')
    else:
      aux=False
      for b in self.boundaryBegin:
        if type(b)!=np.bool_:
          check=False
          aux=True
          pass
        pass
      if aux is True:
        msg.append('beam.boundaryBegin components are not bool')
        pass
      pass
    if self.dof is not None:
      if self.boundaryBegin.shape[0]!=self.dof:
        check=False
        msg.append('beam.boundaryBegin has not {}(=dof) dimensions'.format(self.dof))
        pass
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('beam Checker')
      pass
    pass
  boundaryEnd=np.zeros(6,dtype=bool)
  def check_boundaryEnd(self):
    check=True
    msg=[]
    if type(self.boundaryEnd)!=np.ndarray:
      check=False
      msg.append('beam.boundaryEnd is not a ndarray (numpy)')
    else:
      aux=False
      for b in self.boundaryEnd:
        if type(b)!=np.bool_:
          check=False
          aux=True
          pass
        pass
      if aux is True:
        msg.append('beam.boundaryEnd components are not a bool')
        pass
      pass
    if self.dof is not None:
      if self.boundaryEnd.shape[0]!=self.dof:
        check=False
        msg.append('beam.boundaryEnd has not {}(=dof) dimensions'.format(self.dof))
        pass
      pass
    if check is False:
      for m in msg:
        print(m)
        pass
      sys.exit('beam Checker')
      pass
    pass
  pointLoads=[]
  def check_pointLoads(self):
    if len(self.pointLoads)>0:
      check=True
      msg=[]
      if type(self.pointLoads)!=list or type(self.pointLoads[0])!=pointLoad:
        check=False
        msg.append('beam.pointLoads is not a list')
      else:
        aux=False
        for pL in self.pointLoads:
          if type(pL)!=pointLoad:
            check=False
            aux=True
            pass
          pass
        if aux is True:
          msg.append('beam.pointLoads components are not pointLoad')
          pass
        for pL in self.pointLoads:
          if pL.value.shape[0]!=self.dof:
            check=False
            aux=True
            pass
          pass
        if aux is True:
          msg.append('beam.pointLoads do not have the same number of dof as the beam')
          pass
        # TODO ANALIZAR ALINEACIÓN DEL PUNTO DE APLICACIÓN CON LA VIGA
      if check is False:
        for m in msg:
          print(m)
          pass
        sys.exit('beam Checker')
        pass
      pass
    pass

  A=np.zeros([dof,2*dof],dtype=float)

  b=np.zeros([dof],dtype=float)[np.newaxis]

  h=None

  staticDetermination=None

  reactionBegin=np.zeros(dof,dtype=float)

  reactionEnd=np.zeros(dof,dtype=float)

  displacementBegin=np.zeros(dof,dtype=float)

  displacementEnd=np.zeros(dof,dtype=float)

  referencePoints=[]

  forces=np.array(6,dtype=piecewiseFunction)[np.newaxis]

  # %% Checker inherited
  # %% Constructor
  def __init__(self,translations=None,rotations=None,line=None,boundaryBegin=None,boundaryEnd=None,
               report=False):
    if line is not None:
      super().__init__(line.begin,line.end)
      pass
    self.translations=translations
    self.rotations=rotations
    self.dof=np.count_nonzero(translations)+np.count_nonzero(rotations)
    self.boundaryBegin=boundaryBegin
    self.boundaryEnd=boundaryEnd
    self.pointLoads=[]
    # A
    self.A=np.zeros([self.dof,2*self.dof])
    Abegin=np.array([[1,0,0, 0,0,0],
               [0,1,0, 0,0,0],
               [0,0,1, 0,0,0],
               [0,0,0, 1,0,0],
               [0,0,0, 0,1,0],
               [0,0,0, 0,0,1]])
    Aend=np.array([[1,0,0, 0,0,0],
               [0,1,0, 0,0,0],
               [0,0,1, 0,0,0],
               [0,0,0, 1,0,0],
               [0,0,-self.l, 0,1,0],
               [0,self.l,0, 0,0,1]])
    # delete not existing dof
    Abegin=self.dofReduction_matrix(Abegin)
    Aend=self.dofReduction_matrix(Aend)
    self.A[0:self.dof,0:self.dof]=np.array(Abegin)
    self.A[0:self.dof,self.dof:2*self.dof]=np.array(Aend)
    # delete not restrained dof
    for i in range(0,len(self.boundaryEnd)):
      bE=self.boundaryEnd[len(self.boundaryEnd)-1-i]
      if not bE:
        self.A=np.delete(self.A,2*self.dof-1-i,axis=1)
        pass
      pass
    for i in range(0,len(self.boundaryBegin)):
      bB=self.boundaryBegin[len(self.boundaryBegin)-1-i]
      if not bB:
        self.A=np.delete(self.A,self.dof-1-i,axis=1)
        pass
      pass
    # b
    self.b=np.zeros([self.dof],dtype=float)[np.newaxis]
    # h
    self.h=self.A.shape[1]-self.A.shape[0]
    # % static setermination
    if self.h==0:
      if np.linalg.det(self.A) == 0:
        self.staticDetermination='Intern Static Indetermination'
        if report: print('Intern Static Indetermination')
        sys.exit()
      else:
        self.staticDetermination='Static Determinated'
        if report: print('Static Determinated')
        pass
    else:
      if self.h>0:
        self.staticDetermination='Extern Static Indetermination'
        if report: print('Extern Static Indetermination')
        sys.exit()
        # hiperstatic
      else:
        self.staticDetermination='Mechanism'
        if report: print('Mechanism')
        sys.exit()
      pass
    # reference points: begin and end
    self.referencePoints=[]
    self.add_referencePoint(self.begin)
    self.add_referencePoint(self.end)
    self.checker()
    pass
  # %% Methods
  # Method: Add point load
  def add_pointLoad(self,pointLoad,report=False):
    if pointLoad is not None:
      xP=self.get_L(self.begin,pointLoad)
      # save load
      self.pointLoads.append(pointLoad)
      if report: print('pointLoad added with position L={} and value={}'.format(xP,pointLoad.value))
      # add reference points
      self.add_referencePoint(point(pointLoad.x,pointLoad.y,pointLoad.z))
      # update b
      bMatrix=np.array([[-1,0,0, 0,0,0],
                 [0,-1,0, 0,0,0],
                 [0,0,-1, 0,0,0],
                 [0,0,0, -1,0,0],
                 [0,0,xP, 0,-1,0],
                 [0,-xP,0, 0,0,-1]])
      bMatrix=self.dofReduction_matrix(bMatrix)
      self.b+=np.dot(bMatrix,pointLoad.value)
      if report: print('b updated to: {}'.format(self.b))
      pass
    self.checker()
    pass
  def add_referencePoint(self,point):
    inList=False
    for p in self.referencePoints:
      if point.x==p.x and point.y==p.y and point.z==point.z:
        inList=True
        pass
      pass
    if not inList:
      self.referencePoints.append(point)
      self.referencePoints.sort(key=lambda x: self.get_L(x,self.begin))
      pass
    pass
  def add_Force(self,interval,forceMatrix,load,new=False,report=False):
    forces=[]
    for i in range(6):
      aux=np.poly1d([0])
      for j in range (6):
        if forceMatrix[i][j]!=0:
          aux+=forceMatrix[i][j]*load[j]
        else:
          aux+=np.poly1d([0])*load[j]
          pass
        pass
      forces.append(aux)
      pass
    for i in range(0,len(forces)):
      force=forces[i]
      if new:
        self.forces[i]=piecewiseFunction(intervals=[interval],values=[force],report=report)
      else:
        if force!=np.poly1d([0]):
          self.forces[i].add_pieces(intervals=[interval],values=[force],report=report)
          pass
        pass
      pass
    pass
  def calculate(self,report=None):
    self.get_Reactions(report=report)
    self.get_Forces(report=report)
    self.get_displacements(report=report)
    pass
  def get_Reactions(self,report=False):
    x = np.dot(np.linalg.inv(self.A),np.transpose(self.b))
    i=0
    # reactionBegin
    rB=np.zeros(self.dof,dtype=float)#[np.newaxis]
    j=0
    for b in self.boundaryBegin:
      if b:
        rB[j]=x[i]
        i+=1
        pass
      j+=1
      pass
    self.reactionBegin=rB
    if report: print('reactionBegin updated to: {}'.format(self.reactionBegin))
    # reactionsEnd
    rE=np.zeros(self.dof,dtype=float)#[np.newaxis]
    j=0
    for b in self.boundaryEnd:
      if b:
        rE[j]=x[i]
        i+=1
        pass
      j+=1
      pass
    self.reactionEnd=rE
    if report: print('reactionEnd updated to: {}'.format(self.reactionEnd))
    pass
  def get_Forces(self,report=False):
    self.forces=np.zeros([6],dtype=piecewiseFunction)#[np.newaxis]
    # reactions forces
    if report: print('Reaction Forces')
    interval=[0,self.l]
    forceMatrix=np.array([[np.poly1d([-1]),0,0, 0,0,0],
           [0,np.poly1d([1]),0, 0,0,0],
           [0,0,np.poly1d([1]), 0,0,0],
           [0,0,0, np.poly1d([-1]),0,0],
           [0,0,np.poly1d([1,0]), 0,np.poly1d([1]),0],
           [0,np.poly1d([1,0]),0, 0,0,np.poly1d([-1])]])
    load=np.transpose(self.dofAmpliation_array(self.reactionBegin))
    if report: print(load,interval)
    self.add_Force(interval,forceMatrix,load,new=True,report=report)
    if report: self.plot_Forces()
    # pointLoads
    if report: print('Point Loads Forces')
    for pointLoad in self.pointLoads:
      xP=self.get_L(self.begin,pointLoad)
      interval=[xP,self.l]
      forceMatrix=np.array([[np.poly1d([-1]),0,0, 0,0,0],
              [0,np.poly1d([1]),0, 0,0,0],
              [0,0,np.poly1d([1]), 0,0,0],
              [0,0,0, np.poly1d([-1]),0,0],
              [0,0,np.poly1d([1,-xP]), 0,np.poly1d([1]),0],
              [0,np.poly1d([1,-xP]),0, 0,0,np.poly1d([-1])]])
      load=np.transpose(self.dofAmpliation_array(pointLoad.value))
      if report: print(load,interval)
      self.add_Force(interval,forceMatrix,load,report=report)
      if report: self.plot_Forces()
      pass
    pass
  def get_displacements(self,report=False):
    A=np.zeros([self.dof,2*self.dof])
    Abegin=np.array([[-1,0,0, 0,0,0],
               [0,-1,0, 0,0,-self.l],
               [0,0,-1, 0,-self.l,0],
               [0,0,0, -1,0,0],
               [0,0,0, 0,-1,0],
               [0,0,0, 0,0,-1]])
    Aend=np.array([[1,0,0, 0,0,0],
               [0,1,0, 0,0,0],
               [0,0,1, 0,0,0],
               [0,0,0, 1,0,0],
               [0,0,0, 0,1,0],
               [0,0,0, 0,0,1]])
    # delete not existing dof
    Abegin=self.dofReduction_matrix(Abegin)
    Aend=self.dofReduction_matrix(Aend)
    A[0:self.dof,0:self.dof]=np.array(Abegin)
    A[0:self.dof,self.dof:2*self.dof]=np.array(Aend)
    # delete restrained dof
    for i in range(0,len(self.boundaryEnd)):
      bE=self.boundaryEnd[len(self.boundaryEnd)-1-i]
      if bE:
        A=np.delete(A,2*self.dof-1-i,axis=1)
        pass
      pass
    for i in range(0,len(self.boundaryBegin)):
      bB=self.boundaryBegin[len(self.boundaryBegin)-1-i]
      if bB:
        A=np.delete(A,self.dof-1-i,axis=1)
        pass
      pass
    # array of integrals
    ctes=np.ones([6],dtype=float)[np.newaxis] #TODO terminos constantes de las integrales
    b=np.zeros([6],dtype=float)[np.newaxis]
    for i in range(0,6):
      force=self.forces[i]
      b[0,i]=force.get_integral(interval=[0,self.l])
      pass
    b=np.multiply(ctes,b)
    b= self.dofReduction_array(b)
    print(A)
    print(b)
    x = np.dot(np.linalg.inv(self.A),np.transpose(self.b))
    print(x)
    i=0
    # displacementBegin
    dB=np.zeros(self.dof,dtype=float)#[np.newaxis]
    j=0
    for b in self.boundaryBegin:
      if b:
        dB[j]=x[i]
        i+=1
        pass
      j+=1
      pass
    self.displacementBegin=dB
    if report: print('displacementBegin updated to: {}'.format(self.displacementBegin))
    # displacementEnd
    dE=np.zeros(self.dof,dtype=float)#[np.newaxis]
    j=0
    for b in self.boundaryEnd:
      if b:
        dE[j]=x[i]
        i+=1
        pass
      j+=1
      pass
    self.displacementEnd=dE
    if report: print('displacementEnd updated to: {}'.format(self.displacementEnd))
    pass
    pass
  def dofAmpliation_array(self,a):
    a=a[np.newaxis]
    if a.shape[0]==1:
      ax=1
    elif a.shape[1]==1:
      ax=0
    else:
      ax=None
      pass
    if not self.translations[0]:
      a=np.insert(a,0,0,axis=ax)
      pass
    if not self.translations[1]:
      a=np.insert(a,1,0,axis=ax)
      pass
    if not self.translations[2]:
      a=np.insert(a,2,0,axis=ax)
      pass
    if not self.rotations[0]:
      a=np.insert(a,3,0,axis=ax)
      pass
    if not self.rotations[1]:
      a=np.insert(a,4,0,axis=ax)
      pass
    if not self.rotations[2]:
      a=np.insert(a,5,0,axis=ax)
      pass
    return a
  def dofAmpliation_matrix(self,M):
    Mamp=np.zeros([6,6],dtype=float)
    i=0
    if not self.translations[0]:
      Mamp[0]=np.zeros([1,6],dtype=float)
    else:
      Mamp[0]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    if not self.translations[1]:
      Mamp[1]=np.zeros([1,6],dtype=float)
    else:
      Mamp[1]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    if not self.translations[2]:
      Mamp[2]=np.zeros([1,6],dtype=float)
    else:
      Mamp[2]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    if not self.rotations[0]:
      Mamp[3]=np.zeros([1,6],dtype=float)
    else:
      Mamp[3]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    if not self.rotations[1]:
      Mamp[4]=np.zeros([1,6],dtype=float)
    else:
      Mamp[4]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    if not self.rotations[2]:
      Mamp[5]=np.zeros([1,6],dtype=float)
    else:
      Mamp[5]=self.dofAmpliation_array(M[i])
      i+=1
      pass
    return Mamp
  def dofReduction_array(self,a):
    if a.shape[0]==1:
      ax=1
    elif a.shape[1]==1:
      ax=0
    else:
      ax=None
      pass
    if not self.rotations[2]:
      a=np.delete(a,5,axis=ax)
      pass
    if not self.rotations[1]:
      a=np.delete(a,4,axis=ax)
      pass
    if not self.rotations[0]:
      a=np.delete(a,3,axis=ax)
      pass
    if not self.translations[2]:
      a=np.delete(a,2,axis=ax)
      pass
    if not self.translations[1]:
      a=np.delete(a,1,axis=ax)
      pass
    if not self.translations[0]:
      a=np.delete(a,0,axis=ax)
    return a
  def dofReduction_matrix(self,M):
    if not self.rotations[2]:
      M=np.delete(M,5,axis=0)
      M=np.delete(M,5,axis=1)
      pass
    pass
    if not self.rotations[1]:
      M=np.delete(M,4,axis=0)
      M=np.delete(M,4,axis=1)
      pass
    if not self.rotations[0]:
      M=np.delete(M,3,axis=0)
      M=np.delete(M,3,axis=1)
    if not self.translations[2]:
      M=np.delete(M,2,axis=0)
      M=np.delete(M,2,axis=1)
      pass
    if not self.translations[1]:
      M=np.delete(M,1,axis=0)
      M=np.delete(M,1,axis=1)
      pass
    if not self.translations[0]:
      M=np.delete(M,0,axis=0)
      M=np.delete(M,0,axis=1)
    return M
  def plot_Forces(self):
    fig, (ax1,ax2,ax3,ax4,ax5,ax6) = plt.subplots(6, 1, sharex=True)
    axList=[ax1,ax2,ax3,ax4,ax5,ax6]
    colorList=['blue','green','green','purple','red','red']
    x_plot = np.arange(0,self.l,0.01,dtype=float)
    y_plot=np.arange(0,len(x_plot),dtype=float)
    for force,ax,color in zip(self.forces,axList,colorList):
      for i in range(0,len(x_plot)):
        y_plot[i]=force.get_value(x_plot[i])
        pass
      ax.plot(x_plot,y_plot,linewidth=1,color=color)
      ax.fill_between(x_plot,0,y_plot,color=color,alpha=0.25)
      pass
    plt.show()
    pass
  pass

