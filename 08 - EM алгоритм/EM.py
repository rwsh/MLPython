#

import numpy as np

import matplotlib.pyplot as pt

import math

X = [[5.4, 4020, 2060, 57, 37],
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

M = len(X)

N = len(X[0])

K = 2

T = 10

Max = []
Min = []

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


def P(k, x, mu, sigma):
    N = len(x)
    
    Sigma = 1
    for n in range(N):
        Sigma *= sigma[k][n]

    res = 0
    for n in range(N):
        res += (x[n] - mu[k][n]) * (x[n] - mu[k][n]) / sigma[k][n]
    res /= -2 #* Sigma 

    res = np.exp(res) / (math.sqrt(Sigma) * math.pow(2 * math.pi, N / 2.0))

    return res

W = []
for k in range(K):
    W.append(1.0 / K)

mu = []
for k in range(K):
    muk = []
    for n in range(N):
        muk.append(X[k][n])
    mu.append(muk)

sigma = []
for k in range(K):
    sigmak = []
    for n in range(N):
        s = 0
        for m in range(M):
            s += (X[m][n] - mu[k][n]) * (X[m][n] - mu[k][n])
        s /= M * K

        s = 1 # !

        sigmak.append(s)
    sigma.append(sigmak)

for t in range(T):
    g = []
    for m in range(M):
        gm = []
        g1 = 0
        for k in range(K):
            g1 += W[k] * P(k, X[m], mu, sigma)

        for k in range(K):
            gm.append(W[k] * P(k, X[m], mu, sigma) / g1)
        g.append(gm)

    for k in range(K):
        W[k] = 0
        for m in range(M):
            W[k] += g[m][k]
        W[k] /= float(M)

        for n in range(N):
            mu[k][n] = 0
            for m in range(M):
                mu[k][n] += g[m][k] * X[m][n]
            mu[k][n] /= M * W[k]

    for k in range(K):
        for n in range(N):
            sigma[k][n] = 0
            for m in range(M):
                sigma[k][n] += g[m][k] * (X[m][n] - mu[k][n]) * (X[m][n] - mu[k][n])
            sigma[k][n] /= M * W[k]

# print(g)

for m in range(M):
    km = 0
    for k in range(K):
        if g[m][k] > g[m][km]:
            km = k
    print("Объект {0} с вероятностью {1} относится к классу {2}".format(m, g[m][km], km))



            