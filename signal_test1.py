#! /usr/bin/python

import sys

import signal_lib
import numpy as np
import matplotlib.pyplot as plt


dt = 0.001
t = np.arange(-10, 10, dt)

S = np.sinc(t)

S *= S

plt.plot(t, S)
plt.show()




