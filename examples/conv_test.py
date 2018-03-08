#! /usr/bin/python

import math
import numpy as np
import matplotlib.pyplot as plt


def integr(s, dt):
    return sum(s) * dt;


def dirac(t, dt, p):
    amp = int(2 * t / dt)
    out = [0] * amp
    
    p = int(p / dt)

    i = 0
    while i < amp:
        out[i] = 1 
        i += p

    return out


def conv(f1, f2, t, dt):
    l = len(t)
    out = [0] * l
    
    if callable(f1):
        v1 = f1(t)
    else:
        v1 = f1

    for i in range(l):
        v2 = f2(t[i] - t)
        tmp = v1 * v2
        out[i] = integr(tmp, dt)

    return out


def rect(t):
    return abs(t) < 0.5 + (0.5 * abs(t) == 0.5)


dt = 0.01
t = np.arange(-10, 10, dt)
d = dirac(10, dt, 2)
c = conv(d, rect, t, dt) 

plt.figure()
plt.plot(t,c)
plt.show()


