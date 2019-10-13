#

import numpy as np

import matplotlib.pyplot as pt

N = 2

M = 100

L = 1000

alpha = 0.95

beta = 0.2

gamma = 0.2

def F(x):

    res = (1 - x[0]) * (1 - x[0]) + 100 * (x[1] - x[0] * x[0]) * (x[1] - x[0] * x[0])

    return res

def CalcMinAll(Xmin):
    Res = Xmin[0]

    for x in Xmin:
        if F(x) < F(Res):
            Res = x

    return Res

X = []
V = []
Xmin = []
XMinAll = np.zeros(N)

for m in range(M):
    x = np.zeros(N)
    x[0] = np.random.uniform(-100, 100)
    x[1] = np.random.uniform(-100, 100)

    X.append(x)    
    Xmin.append(x)

    v = np.zeros(N)
    v[0] = np.random.uniform(-10, 10)
    v[1] = np.random.uniform(-10, 10)

    V.append(v)

XMinAll = CalcMinAll(Xmin)

for l in range(L):
    for m in range(M):
        V[m] = alpha * V[m] + beta * np.random.uniform() * (Xmin[m] - X[m]) + gamma * np.random.uniform() * (XMinAll - X[m])

        X[m] = X[m] + V[m]

        if F(X[m]) < F(Xmin[m]):
            Xmin[m] = X[m]

    XMinAll = CalcMinAll(Xmin)

print("{0}\tЗначение = {1}".format(XMinAll, F(XMinAll)))


