# -*- coding: utf-8 -*-

"""
Сеть Хопфилда

Разработчик: Р.В. Шамин

www.shamin.ru, roman@shamin.ru
"""

import numpy as np

X = [[1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
     [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1]]

N = len(X[0])

W = np.zeros((N, N), 'float')

for x in X:
    for i in range(N):
        for j in range(N):
            W[i, j] = W[i, j] + x[i] * x[j]
            if i == j:
                W[i, j] = 0

W = W / N

Y = [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1]

L = 100

IsEq = True

for l in range(L):
    Z = []
    for j in range(N):
        d = 0
        for i in range(N):
            d = d + W[i, j] * Y[i]
        
        if d > 0:
            Z.append(1)
        else:
            Z.append(-1)
    for x in X:
        IsEq = True
        for i in range(N):
            if x[i] != Z[i]:
                IsEq = False
                break
        if IsEq:
            print("\n\nОбраз найден!\n")
            print(x) 
            print(Z) 
            break
    if IsEq:
        break
if not IsEq:
    print("Образ не найден.")
        

  
