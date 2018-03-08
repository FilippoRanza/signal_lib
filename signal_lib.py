try:
    import math
    import numpy as np
    import scipy
except ImportError:
    msg = "numpy and scipy are necessary for this library"
    raise ImportError(msg)

def hyperbole(t, m=100):
    out = 1 / t
    if m < 0:
        return out
    for i in range(len(t)):
        if abs(out[i]) > m:
            s = np.sign(out[i])
            out[i] = m * s
    return out
     


def integr(s, dt):
    return sum(s) * dt


def dirac(t):
    return t == 0 * 1

def dirac_set(t, p, dt=0):
    l = len(t)
    i = 0

    if dt:
        p = int(p / dt)
    i = 0
    out = [0] * l
    while i < l:
        out[i] = 1
        i += p

    return out




def conv(s1, s2, t, dt):
    
    l = len(t)
    out = [0] * l
    
    if callable(s1):
        v1 = s1(t)
    else:
        v1 = s1

    for i in range(l):
        v2 = s2(t[i] - t)
        tmp = v1 * v2
        out[i] = integr(tmp, dt)

    return out


def fourier(s, f, df, sign):
    l = len(f)
    out = [0] * l
    
    if callable(s):
        v = s(f)
    else:
        v = s    
    
    for i in range(l):
        arg = sign * 1j * 2 * math.pi * f[i]  * f
        e = np.exp(arg)
         
        tmp = v * e
        
        out[i] = integr(tmp, df)

    return out

def time_to_freq(s, f, df):
   return fourier(s, f, df, -1)

def freq_to_time(s, t, dt):
    return fourier(s, t, dt, 1)


def rect(t):
    a = abs(t)
    return (a < 0.5 ) + ( 0.5 * (a == 0.5))


def tri(t):
    a = abs(t)
    return (a <= 1) * (1 - a)


def period(s, p, t, dt):
    dp = dirac_set(t, p, dt)
    return conv(dp, s, t,dt)

    
    
        

def norm(s, dt):
    s = abs(s) 
    tmp = integr(s, dt)
    return  tmp

def norm2(s, dt):
    s = abs(s) ** 2
    tmp = integr(s, dt)
    return np.sqrt(tmp)


def scal(s1, s2, dt):
    arg = s1 * s2
    return integr(arg, dt)

def corr(s1, s2, t, dt):
    
    if callable(s1):
        v1 = np.conj(s1(t))
    else:
        v1 = np.conj(s1)

    l = len(t)
    out = [0] * l
    for i in range(l):
        tmp = s2(t + t[i])
        arg = v1 * tmp
        out[i] = integr(arg, dt)

    return out

def epsilon(t):
    return ((t > 0) + ((0.5) * t == 0)) * 1



def mkTime(span, dt):
    return np.arange(-span, span, dt)



class Signals:
    
    def addSignal(self, s, name=None, t=None, overwrite=False):
        
        if not overwrite and name in self.signals.keys():
            print("signal {} already exists".format(name))
            print("this index will not be overwritten")
            print("use overwrite=True to enable overwrite")
            return

        
        if callable(s):
            if t == None:
                t = self.t
            v = s(t)
        else:
            v = s
        if name == None:
            name = "signal_{}".format(self.count)
            self.count += 1
                  
        self.signals[name] = s
        if self.verbose:
            print("adding new signal as {}".format(name))

    def get(self, name):
        if name in self.signals.keys():
            return self.signals[name]
        return None

    def list(self):
        return self.signals.keys()

    def integr(self, name, dt=None):
        if name in self.signals.keys():
            s = self.signals[name]
            if dt == None:
                dt = self.dt
            return integr(s, dt)

        return None

    

    def __init__(self, span, dt, verbose=False):
        self.t = mkTime(span, dt)
        self.dt = dt

        self.signals = {}
        self.count = 0

        self.verbose = verbose
   





