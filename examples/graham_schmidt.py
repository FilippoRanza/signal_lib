#! /usr/bin/python

"""
Calcola l'ortogoanlizzazione di Graham-Schmidt di un vettore di segnali
"""

import numpy as np
import signal_lib as sl
import math
import matplotlib.pyplot as plt




def normalize(s, dt):
    n = sl.norm2(s, dt)
    return (s / n)

def reduce(s1, s2, dt):
    s = sl.scal(s1, s2, dt)
    s2 *= s
    return s2

def orto(l, dt):
    
    out = [0] * len(l)

    out[0] = normalize(l[0], dt)

    for i in range(1, len(l)):
        tmp = [0] * len(l[0])
        for j in range(i):
            tmp += reduce(l[i], l[j], dt)

        tmp = l[i] - tmp
        out[i] = normalize(tmp, dt)
    
    return out


dt = 0.01
t = np.arange(-10, 10, dt)

v1 = 2 * sl.rect(t) 
v2 = sl.rect(t - 0.5) * sl.tri(t) + sl.tri(t- 1)


o = orto([v1, v2], dt)

#plt.figure()

plt.plot(t,o[0])
plt.show()

plt.plot(t,o[1])
plt.show()


for i in o:
    print(sl.norm(i, dt))

print(sl.scal(o[0], o[1], dt))

"""
print(sl.norm(v1, dt))
v1 /= 1.5
print(sl.norm(v1, dt))


s = sl.scal(v1, v2, dt)
print(s)

v2 -= v1 * s

s = sl.scal(v1, v2, dt)
print(s)
"""






