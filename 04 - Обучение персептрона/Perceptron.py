#

import numpy as np

import matplotlib.pyplot as pt

N = 2

M = 100

L = 10

alpha = 0.1

X = []

for m in range(M):
    X.append((np.random.randint(0, 100), np.random.randint(0, 100)))

def d(x):
    if x[0] <= x[1]:
        return -1
    else:
        return 1

def sign(w, x):
    res = 0
    for n in range(N):
        res += w[n] * x[n]

    if res < 0:
        return -1
    else:
        return 1

w = []

for n in range(N + 1):
    w.append(0)

for l in range(L):
    for x in X:
        y = sign(w, x)

        dm = d(x)

        if dm * y < 0:
            w[N] += alpha * alpha * dm
            for n in range(N):
                w[n] += alpha * dm * x[n]

print(w)



