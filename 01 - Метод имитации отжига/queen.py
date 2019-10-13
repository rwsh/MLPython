
import numpy as np

import matplotlib.pyplot as pt

N = 8

Pos = []

for n in range(N):
    Pos.append(n)


def H(Pos):
    res = 0
        
    for n in range(N):
        k = n - 1
        while k >= 0:
            if Pos[k] == (Pos[n] + (n - k)):
                res = res + 1

            if Pos[k] == (Pos[n] - (n - k)):
                res = res + 1
            k = k - 1

        k = n + 1
        while k < N:
            if Pos[k] == (Pos[n] + (k - n)):
                res = res + 1

            if Pos[k] == (Pos[n] - (k - n)):
                res = res + 1
            k = k + 1
                
    return res

def G(Pos):
    i = 0
    j = 0
    while i == j:
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
            
    a = Pos[i]
    Pos[i] = Pos[j]
    Pos[j] = a
    
    return Pos


T0 = 100

alpha = 0.95

k = 0

T = T0

s = 10

T = alpha * T

L = 200

t = []
x = []
Hx = []

T0 = 100

alpha = 0.98

k = 0

T = T0

s = Pos

T = alpha * T

L = 1000

for i in range(L):

    if H(s) == 0:
        break

    s_ = G(s)

    Delta = H(s_) - H(s)

    if Delta < 0:
        s = s_
    else:
        if np.random.uniform(0, 1) < np.exp(-Delta / T):
            s_ = s

    t.append(i)
    Hx.append(H(s))

print("Найденный вариант = {0}; значение = {1}".format(s, H(s)))

pt.plot(t, Hx)

pt.grid(True)

pt.show()




