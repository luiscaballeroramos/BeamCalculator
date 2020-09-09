import numpy as np

def angle(a,b):
  return np.degrees(np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))))

x0=np.array([1,0,0])
y0=np.array([0,1,0])
z0=np.array([0,0,1])

def R(ang1,ang2,ang3):
  sin1=np.sin(np.deg2rad(ang1))
  cos1=np.cos(np.deg2rad(ang1))

  sin2=np.sin(np.deg2rad(ang2))
  cos2=np.cos(np.deg2rad(ang2))

  sin3=np.sin(np.deg2rad(ang3))
  cos3=np.cos(np.deg2rad(ang3))

  R1=np.array([[1,0,0],
             [0,cos1,sin1],
             [0,-sin1,cos1]])
  R2=np.array([[cos2,0,-sin2],
             [0,1,0],
             [sin2,0,cos2]])
  R3=np.array([[cos3,sin3,0],
             [-sin3,cos3,0],
             [0,0,1]])

  return np.dot(np.dot(R1,R2),R3)

v0=np.array([10,10,10])
pro=np.array([v0[0],v0[1],0])

ang3=angle(x0,pro)
if np.cross(x0,pro)[2]<0:
  ang3=-ang3
  pass

ang2=angle(pro,v0)
if np.cross(np.dot(R(0,0,ang3),pro),np.dot(R(0,0,ang3),v0))[1]<0:
  ang2=-ang2
  pass

R2=R(0,ang2,ang3)
v2=np.dot(R2,v0)

print(v2)

