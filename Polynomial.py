import numpy as np
# creation
p=np.poly1d([1,2,3],variable='y')
print(p)
# creation by roots
q=np.poly1d([1,-3,2],True)
print(q)
# coefficients
print(p.c)
print(p[1])
# evaluate
print(p(0.5))
# roots
print(p.r)
# operations
print(p**2)
print(p*p)
print((p+5)/(p-np.poly1d([1,0])))

# derivative
print(q.deriv(2))
print(q.integ())

from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
w = Symbol('w')
u = Symbol('u')
q = Symbol('q')
e = Symbol('e')

f = x**3 + x*y**4 + x*z**2*w + u*q**2*w*e**3

f2 = (f*f)

F = integrate(f, x)
G = integrate(f, y)



# %%
xx = np.linspace(-5, 5)
yy = np.piecewise(xx, [xx<0, xx>=0], [lambda xx: -xx, lambda xx: xx])



# %%
import sympy as sym
x = sym.symbols('x')

f=x**2
g=x

expresion1=sym.functions.elementary.piecewise.ExprCondPair(g,And(x>=0.5,x<=1.5))
expresion2=sym.functions.elementary.piecewise.ExprCondPair(f,And(x>=1,x<=2))
f1 = sym.Piecewise(expresion1,(0,True))
f2 = sym.Piecewise(expresion2,(0,True))
print(f1+f2)
print(piecewise_fold(f1+f2))
print(piecewise_fold(f1+f2).subs(x,1.50000001))
print(sym.integrate(piecewise_fold(f1+f2),(x,0,6)))

# %%
from sympy import symbols, Matrix
from numpy import trace
x, y, a, b = symbols('x y a b')
M = Matrix(([x, y], [a, b]))
M
print(trace(M))
print(M.dot(M))

M.dot(M)[0][0]


# %%
import numpy as np
# reactionMatrix=np.array([[-1,0,0, 0,0,0],
#        [0,-1,0, 0,0,0],
#        [0,0,-1, 0,0,0],
#        [0,0,0, -1,0,0],
#        [0,0,2, 0,-1,0],
#        [0,2,0, 0,0,-1]])
# interval=[0,10]
# fuerza=np.array([1,1,1,1,1,1])
# forces=np.dot(reactionMatrix,fuerza)

a=[[np.poly1d([1,1]),np.poly1d([0])],
      [np.poly1d([3,3]),np.poly1d([4,4])]]

b=[1,2]

res2=[]
for i in range(2):
  res1=0
  for j in range (2):
    res1+=a[i][j] * b[j]
    print(a[i][j] * b[j])
    pass
  res2.append(res1)
  pass
print(res2[0],res2[1])

# %%
import numpy as np
from Piecewise import *

function=piecewiseFunction([[0,2]],[np.poly1d([1,0])])

print(function.get_integral())











