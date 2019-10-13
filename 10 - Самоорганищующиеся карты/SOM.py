#

import numpy as np

import matplotlib.pyplot as pt

import copy

import math

XA = [[5.4, 4020, 2060, 57, 37],
     [8.9, 4810, 2223, 140, 40],
     [19.5, 5380, 2910, 285, 60],
     [25, 5890, 2880, 300, 40],
     [44.8, 6870, 3270, 700, 55],
     [56, 6316, 3705, 700, 44],
     [68, 7380, 3755, 700, 38],
     [13.8, 5200, 2470, 300, 60],
     [9.2, 4285, 2348, 140, 42],
     [30, 5920, 3000, 500, 54],
     [31.8, 6070, 3180, 500, 60],
     [47.5, 6675, 3320, 600, 34],
     [44.2, 6770, 3070, 520, 37],
     [46, 6770, 3070, 520, 37],
     [49, 6900, 3150, 520, 40]]

X = copy.deepcopy(XA)

K = len(X)

N = len(X[0])

MM = 10

M = MM * MM

T = 10000

Max = []
Min = []

eta0 = 0.1

a = 5E-4

sigma0 = 20

b = 1.3E-3

def eta(t):
    return eta0 * math.exp(-a * t)

def h(t, r):
    return math.exp(-(r * r) / (2 * sigma(t)))

def sigma (t):
    return sigma0 * math.exp(-b * t)


def rhoN(x, y):
    res = 0

    for n in range(len(x)):
        res += abs(x[n] - y[n])

    return res

def rho(m1, m2):
    xy1 = divmod(m1, MM)
    xy2 = divmod(m2, MM)

    return math.sqrt((xy1[0] - xy2[0]) * (xy1[0] - xy2[0]) + (xy1[1] - xy2[1]) * (xy1[1] - xy2[1]))

def NearN(x, W):
    res = 0
    min = rhoN(x, W[0])

    for m in range(M):
        #print(rhoN(x, W[m]))
        if rhoN(x, W[m]) < min:
            min = rhoN(x, W[m])
            res = m
            
    return res

for n in range(N):
    Max.append(X[0][n])
    Min.append(X[0][n])

    for m in range(K):
        if X[m][n] > Max[n]:
            Max[n] = X[m][n]
        if X[m][n] < Min[n]:
            Min[n] = X[m][n]


An = []
Bn = []

for n in range(N):
    an = 1 / (Max[n] - Min[n])
    bn = -Min[n] / (Max[n] - Min[n])
    An.append(an)
    Bn.append(bn)

    for m in range(K):
        X[m][n] = an * X[m][n] + bn


W = []

for m in range(M):
    Wm = []
    for n in range(N):
        Wm.append(np.random.uniform(0, 1))
    W.append(Wm)

t = 1

while t < T:
    k = np.random.randint(0, K)

    m_ = NearN(X[k], W)

    eta_t = eta(t)
    
    for m in range(M):
        for n in range(N):
            W[m][n] += eta_t * h(t, rho(m, m_)) * (X[k][n] - W[m][n])

    t += 1

print(W)

for x in X:
    m = NearN(x, W)

    print(divmod(m, MM))