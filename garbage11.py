# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:06:10 2019

@author: 180218
"""

from temp_package import *
import numpy as np
import matplotlib.pyplot as plt


Reader.figure(path='./esti_cad.csv')
esti_raw=Reader.export()
temp=np.diff(esti_raw[:,0])
temp=np.hstack((np.zeros(1),temp))
mk=temp!=0

esti_raw=esti_raw[mk,:]

plt.plot(esti_raw[:,0]/1000,esti_raw[:,10])
#plt.show()

tt=esti_raw[-1,0]/1000
Reader.figure(path='./ref_cad.csv')
ref_cad=Reader.export()

ref_samplerate=152/len(ref_cad)
ref_ts=np.linspace(0,tt,len(ref_cad))
plt.plot(ref_ts,ref_cad[:,0])
plt.show()


#plt.plot(raw[:,3])
#filter(5)
#filter?
#
#from scipy import signal
#xs = np.arange(0, np.pi*5, 0.05)
#data = np.sin(xs)
#peakind = signal.find_peaks_cwt(data, np.arange(1,10))
#plt.plot(xs,data)
#peakind, xs[peakind], data[peakind]
#xs[peakind]
#data[peakind]
#([32], array([ 1.6]), array([ 0.9995736]))