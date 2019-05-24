# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:45:44 2019

@author: 180218
"""
import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(100)
#
#y = np.exp(x)
#plt.figure(0)
#plt.plot(x, y)
#
#z = np.sin(x)
#plt.figure(1)
#plt.plot(x, z)
#
#w = np.cos(x)
#plt.figure(0) # Here's the part I need
#plt.plot(x, w)
#
x = np.arange(1, 10)
y = x.reshape(-1, 1)
h = x * y

cs = plt.contourf(h, levels=[10, 30, 50],
    colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
cs.cmap.set_over('red')
cs.cmap.set_under('blue')
cs.changed()