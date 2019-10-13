# -*- coding: utf-8 -*-

"""
Обучение с подкреплением

Разработчик: Р.В. Шамин

www.shamin.ru, roman@shamin.ru
"""

import numpy as np

import random as rnd

A = ['L', 'R']

Qsa = {}

def CalcQsa(s, a):
    k = s.__str__() + a
    
    if k in Qsa:
        return Qsa[k]
    else:
        return 0
    
def Chois(s, Eps):
    if rnd.random() < Eps:
        ind = rnd.randint(0, 1)
        return A[ind]
    else:
        if CalcQsa(s, 'L') > CalcQsa(s, 'R'):
            return 'L'
        else:
            return 'R'
    
    
def Run(s, a):
    if s == 1 and a == 'L':
        return (2, 0)
    if s == 1 and a == 'R':
        return (3, 0)
        
    if s == 2 and a == 'L':
        return (4, 0)
    if s == 2 and a == 'R':
        return (5, 0)
        
    if s == 3 and a == 'L':
        return (6, 0)
    if s == 3 and a == 'R':
        return (7, 0)
        
    if s == 4 and a == 'L':
        return (8, 0)
    if s == 4 and a == 'R':
        return (9, 0)
        
    if s == 5 and a == 'L':
        return (10, 0)
    if s == 5 and a == 'R':
        return (11, 0)
        
    if s == 6 and a == 'L':
        return (12, 0)
    if s == 6 and a == 'R':
        return (13, 0)
        
    if s == 7 and a == 'L':
        return (14, 0)
    if s == 7 and a == 'R':
        return (15, 10)
        
    

Eps = 0.2

L = 1000

Alpha = 0.1

Gamma = 0.9

for l in range(L):
    s = 1
    
    a = Chois(s, Eps)
    
    while(True):
        s1, r = Run(s, a)
        
        a1 = Chois(s1, Eps)
        
        k = s.__str__() + a
        k1 = s1.__str__() + a1
        
        Qsa[k] = CalcQsa(s, a) + Alpha * (r + Gamma * CalcQsa(s1, a1) - CalcQsa(s, a))
        
        s = s1
        a = a1
        
        if s > 7:
            break
    
print(Qsa)


s = 1

a = Chois(s, 0)

while(True):
    s, r = Run(s, a)
    print('{0} | {1}'.format(s, a))
    
    a = Chois(s, 0)
    
    if s > 7:
        break
                       
