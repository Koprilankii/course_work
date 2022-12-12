from sympy.stats import QuadraticU, density
from sympy import pprint
  
z = 2.5
a = 12
b = 15
  
# Using sympy.stats.QuadraticU() method
X = QuadraticU("x", a, b)
gfg = density(X)(z)
  
pprint(gfg)