#

import numpy as np

import matplotlib.pyplot as pt

import copy

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

M = len(X)

N = len(X[0])

K = 2

T = 10

la = 0.3

dla = 0.05

Max = []
Min = []

def rho(x, y):
    res = 0

    for n in range(len(x)):
        res += abs(x[n] - y[n])

    return res

def Near(x, W):
    res = 0

    min = rho(x, W[0])

    for k in range(len(W)):
        if rho(x, W[k]) < min:
            min = rho(x, W[k])
            res = k

    return res

for n in range(N):
    Max.append(X[0][n])
    Min.append(X[0][n])

    for m in range(M):
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

    for m in range(M):
        X[m][n] = an * X[m][n] + bn

W = []
for k in range(K):
    w = []
    for n in range(N):
        w.append(np.random.uniform(0.1, 0.3))
    W.append(w)

while la > 0:
    for t in range(T):
        for m in range(M):
            k = Near(X[m], W)
            for n in range(N):
                W[k][n] += la * (X[m][n] - W[k][n])

    la -= dla

for m in range(M):
    k = Near(X[m], W)

    print("Класс = {0}\t{1}".format(k, XA[m]))


