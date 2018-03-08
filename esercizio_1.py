#! /usr/bin/python

"""
z(t) = s1(t) * y(t)

vedi esercitazione in fondo al quadreno per
maggiori spiegazioni

"""

import signal_lib as sl
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(-10, 10, dt)


#sign_1 calcola la funzione s1
sign_1 = lambda t : np.exp(-np.pi * t) * sl.epsilon(t)
s1 = sign_1(t)

#sign_2 calcola la funzione s2
sign_2 = lambda t : np.sin(np.pi * t)
y = sign_2(t)

#traformate di fourier di s1 ed y
S1 = sl.time_to_freq(s1, t, dt)
Y  = sl.time_to_freq(y, t, dt)

#calcola z tramite la convoluzione  e relativa tdf
za = sl.conv(s1, sign_2, t, dt)
ZA = sl.time_to_freq(za, t, dt)
 
#calcola tdf di z tramite prodotto delle trasformate di y ed s1
Y = np.asarray(Y)
S1 = np.asarray(S1)

ZB = Y * S1


#calcola z tramite la funzione analitica ottenuta anti trasformando
sign_3 = lambda t : (1 /(np.sqrt(2)*np.pi)) * np.sin((np.pi * t) - np.pi / 4)
zc = sign_3(t)

#visualizza i risultati ottenuti

plt.plot(t, ZA)
plt.show()

plt.plot(t, ZB)
plt.show()


plt.plot(t,za)
plt.show()


plt.plot(t,zc)
plt.show()






