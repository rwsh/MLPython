#

import numpy as np

import matplotlib.pyplot as pt

L = 1000

M = 100

Mc = 20

N = 5

X = []

def F(x):
    res = 0
    for xn in x:
        res += xn * xn * (1 + np.abs(np.sin(100 * xn)))

    return res

def Fit(x):
    return 1.0 / (1 + F(x))

def Sorting(X):
    Res = X
    for m in range(M - 1):
        for i in range(M - m - 1):
            if Fit(Res[i]) < Fit(Res[i + 1]):
                c = Res[i]
                Res[i] = Res[i + 1]
                Res[i + 1] = c
    return Res

def Cross(A, B):
    Res = []

    p = Fit(A) / (Fit(A) + Fit(B))

    for n in range(N):
        if np.random.uniform(0, 1) < p:
            Res.append(A[n])
        else:
            Res.append(B[n])

    return Res

def New():
    x = []
    for n in range(N):
        x.append(np.random.uniform(-1, 1))
    return x

for m in range(M):
    x = New()
    X.append(x)

for l in range(L):
    X = Sorting(X)
    for m in range(1, M - Mc):
        X[m] = Cross(X[m], X[np.random.randint(0, M)])

    for m in range(M - Mc, M):
        X[m] = New()

print(F(X[0]))
