import sympy as sp
from sympy import physics as spp
from sympy.physics import vector as sppv


# Set manufactured solution
u0, v0, p0, epsilon = sp.symbols('u0, v0, p0, epsilon')

R = sppv.ReferenceFrame('R')

x = R[0]

y = R[1]

u = [0, 0]

u[0] = u0*(sp.sin(x**2 + y**2) + epsilon)

u[1] = v0*(sp.cos(x**2 + y**2) + epsilon)

p = p0*(sp.sin(x**2 + y**2) + 2)


# Print in muparser format
print("\nManufactured solution:")

print(("Function expression = "+str(u[0])+"; "+str(u[1])+"; "+str(p)).replace('**', '^').replace('R_', ''))


# Derive manufactured source term
# @todo For now I'm not taking the symmetric part of the stress tensor, because this is complicating the symbolic implementation.
Re, mu = sp.symbols('Re, mu')

gamma = sp.symbols('gamma')

grad_p = sppv.gradient(p, R).to_matrix(R)

f0 = sppv.dot(u[0]*R.x + u[1]*R.y, sppv.gradient(u[0], R)) - sppv.divergence(mu*sppv.gradient(u[0], R), R) + grad_p[0]

f1 = sppv.dot(u[0]*R.x + u[1]*R.y, sppv.gradient(u[1], R)) - sppv.divergence(mu*sppv.gradient(u[1], R), R) + grad_p[1]

f2 = sppv.divergence(u[0]*R.x + u[1]*R.y, R) + gamma*p


# Print in muparser format
print("\nDerived manufactured source:")

print(("Function expression = "+str(f0)+"; "+str(f1)+"; "+str(f2)).replace('**', '^').replace('R_', ''))