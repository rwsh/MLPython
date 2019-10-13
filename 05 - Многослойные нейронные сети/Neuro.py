#

import numpy as np

import matplotlib.pyplot as pt

XY = []

XY.append([[1, 1, 1, 1, 0, 0, 0, 0], [0]])
XY.append([[0, 0, 0, 0, 1, 1, 1, 1], [1]])

L = len(XY)

N = len(XY[0][0])
M = len(XY[0][1])

H = N

K = 1000

a = 20

eta = 0.0001

def sigma(x):
    return 1 / (1 + np.exp(-a * x))

def dsigma(x):
    return a * sigma(x) * (1 - sigma(x))

W1 = []

for n in range(N + 1):
    A = []
    for h in range(H):
        A.append(np.random.uniform(-1/(2*N), 1/(2*N)))
    W1.append(A)

W2 = []

for h in range(H + 1):
    A = []
    for m in range(M):
        A.append(np.random.uniform(-1/(2*H), 1/(2*H)))
    W2.append(A)

for k in range(K):
    xy = XY[np.random.randint(L)]

    O = []
    Z = []

    for h in range(H):
        o = 0
        for n in range(N):
            o += W1[n][h] * xy[0][n]
        o += W1[N][h]

        O.append(o)
        Z.append(sigma(o))

    O2 = []
    A = []
    for m in range(M):
        o2 = 0
        for h in range(H):
            o2 += W2[h][m] * Z[h]
        o2 += W2[H][m]
        O2.append(o2)
        A.append(sigma(o2))

    E = []
    for m in range(M):
        E.append(A[m] - xy[1][m])

    E2 = []
    for h in range(H):
        e2 = 0
        for m in range(M):
            e2 += E[m] * dsigma(O2[m]) * W2[h][m]
        E2.append(e2)

    for h in range(H):
        for m in range(M):
            W2[h][m] -= eta * E[m] * dsigma(O2[m]) * Z[h]

    for m in range(M):
        W2[H][m] -= eta * E[m] * dsigma(O2[m]) * (1)

    for n in range(N):
        for h in range(H):
            W1[n][h] -= eta * E2[h] * dsigma(O[h]) * xy[0][n]

    for h in range(H):
        W1[N][h] -= eta * E2[h] * dsigma(O[h]) * (1)

#B = [1, 1, 1, 1, 0, 0, 0, 0]
B = [1, 1, 0, 0, 1, 1, 1, 1]

O = []
Z = []

for h in range(H):
    o = 0
    for n in range(N):
        o += W1[n][h] * B[n]
    o += W1[N][h]

    O.append(o)
    Z.append(sigma(o))

O2 = []
A = []
for m in range(M):
    o2 = 0
    for h in range(H):
        o2 += W2[h][m] * Z[h]
    o2 += W2[H][m]
    O2.append(o2)
    A.append(sigma(o2))

print(A)




