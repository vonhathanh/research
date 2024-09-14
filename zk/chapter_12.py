import numpy as np
from py_ecc.bn128 import multiply, G1
from scipy.interpolate import lagrange

# prover: I know the result of this polynomial: out = (x_1)^2 + 4(x_2)^2(x_1) - 2
# break the above equation to quadratic constraints:
# x_3 = x_1*x_1
# x_4 = x_2*x_2
# out - x_3 +2 = 4x_4*x_1
# witness vectors s: [1, out, x_1, x_2, x_3, x_4]
# Our L, R, O matrices must have 3 rows and 6 columns
# Apply the left-right hand rule we learned in chapter 10, we got
L = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 4]])
R = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0]])
O = np.array([[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [2, 1, 0, 0, -1, 0]])

# test our hypothesis
x_1 = 3
x_2 = 4

x_3 = x_1*x_1
x_4 = x_2*x_2
out = 4*x_4*x_1 - 2 + x_3

witness = np.array([1, out, x_1, x_2, x_3, x_4])

assert all(np.equal(np.matmul(L, witness) * np.matmul(R, witness), np.matmul(O, witness))), "not equal"

# Next, we transform the columns from vectors to polynomial
# Start with L, zero vectors turn to zero polynomials, we'll skip doing that here
# With vector [1, 0, 0], we need a polynomial that travel through (1, 1), (2, 0), (3, 0)
xs = [1, 2, 3]
ys = [[1, 0, 0], [0, 1, 0], [0, 0, 4]]
for y in ys:
    p = lagrange(xs, y)
    print(p.c)

ys = [[1, 0, 1], [0, 1, 0]]
for y in ys:
    p = lagrange(xs, y)
    print(p.c)

ys = [[0, 0, 2], [0, 0, 1], [1, 0, -1], [0, 1, 0]]
for y in ys:
    p = lagrange(xs, y)
    print(p.c)

# everything we've done so far is public, what remain hidden is the witness vector, let's pick x_1 = 3, x_2 = 4
# so our witness vector is [1, 199, 3, 4, 9, 16]
Ua = np.array([[0, 0, 0.5, -1, 0, 2],
                [0, 0, -2.5, 4, 0, -6],
                [0, 0, 3, -3, 0, 4]])

witness = [1, 199, 3, 4, 9, 16]

U = (np.matmul(Ua, witness))

Va = np.array([[0, 0, 1, -1, 0, 0],
               [0, 0, -4, 4, 0, 0],
               [0, 0, 4, -3, 0, 0]])

V = (np.matmul(Va, witness))
# array([-1,  4,  0])

Wa = np.array([[1, 0.5, 0, 0, 0, -1],
               [-3, -1.5, 0, 0, -1, 4],
               [2, 1, 0, 0, 2, -3]])

W = (np.matmul(Wa, witness))
# array([  84.5, -246.5,  171. ])

u = np.poly1d(U)
v = np.poly1d(V)
w = np.poly1d(W)

print(u, v, w)

t = np.poly1d([1, -1]) * np.poly1d([1, -2]) * np.poly1d([1, -3])
print(t)

h = (u*v - w) / t
h = h[0]

# last step, pick a random t and perform encrypted polynomial evaluation
# let's pick t = 5, we got:
X = multiply(G1, 5)
X2 = multiply(G1, 5 ** 2)
X3 = multiply(G1, 5 ** 3)
X4 = multiply(G1, 5 ** 4)
