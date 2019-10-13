# Метод имитации отжига
#
# Copuright (c), 2019 Роман Шамин roman@shamin.ru
#
# www.shamin.ru, ai.lector.ru
#

import numpy as np

import matplotlib.pyplot as pt

# оптимизируемая функция
def H(x):
    return x * x * (2 + np.abs(np.sin(8.0 * x)))

def G(x):
    return x + np.random.uniform(-1, 1)

T0 = 100

alpha = 0.95

k = 0

T = T0

s = 10

T = alpha * T

L = 100

t = []
x = []
Hx = []

for i in range(L):

    s_ = G(s)

    Delta = H(s_) - H(s)

    if Delta < 0:
        s = s_
    else:
        if np.random.uniform(0, 1) < np.exp(-Delta / T):
            s_ = s

    t.append(i)
    x.append(s)
    Hx.append(H(s))

pt.plot(t, x)

pt.grid(True)

pt.show()

pt.clf()

pt.plot(t, Hx)

pt.grid(True)

pt.show()






