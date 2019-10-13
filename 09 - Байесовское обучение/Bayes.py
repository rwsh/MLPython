#

import numpy as np

import matplotlib.pyplot as pt

A = [[0.3, 0.2, 0.5, 0.15], 
     [0.6, 0.5, 0.4, 0.3]]

P = [0.6, 0.4]

D = [True, False, True, False]

M = len(A)

N = len(A[0])

AD = P.copy()

for m in range(M):

    for n in range(N):
        if D[n]:
            AD[m] *= A[m][n]
        else:
            AD[m] *= (1 - A[m][n])

S = 0
for p in AD:
    S += p

for m in range(M):
    AD[m] /= S

print(AD)

mmax = 0
mp = AD[0]

for m in range(M):
    if AD[m] > mp:
        mmax = m
        mp = AD[m]

print("Наиболее вероятная гипотеза {0}, с вероятностью {1}".format(mmax, mp))


