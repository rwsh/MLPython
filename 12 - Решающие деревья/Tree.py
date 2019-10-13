#

import numpy as np

import matplotlib.pyplot as pt

import math

def Disp(L):

    E = 0

    for l in L:
        E += l

    E /= len(L)

    D = 0

    for l in L:
        D += (l - E) * (l - E)

    D /= len(L)

    return (E, D)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = [1, 1, 1, 1, 1, 0, 0, 0]


def Split(L, k):
    Left = L[:k]
    Right = L[k:]

    return (Left, Right)

def OptSplit(L):

    if Disp(L)[1] == 0:
        return

    Optk = 1

    OptD = Disp(Split(L, Optk)[0])[1] + Disp(Split(L, Optk)[1])[1]

    for k in range(1, len(L)):
        D = Disp(Split(L, k)[0])[1] + Disp(Split(L, k)[1])[1]

        if D < OptD:
            OptD = D
            Optk = k

    (Left, Right) = Split(L, Optk)

    print("Левое множество:")
    print(Left)

    print("Правое множество:")
    print(Right)

    OptSplit(Left)

    OptSplit(Right)


OptSplit(L)

