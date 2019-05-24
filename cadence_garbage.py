# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:29:36 2019

@author: 180218
"""

from temp_package import *

import numpy as np
import matplotlib.pyplot as plt
import copy
#duration=10
samplerate=500
cadence_max=60 #轉/分
cadence_min=30 #轉/分
noisy=10 #越小nosie越大
cumsum=0
ll=50

cadence=np.random.randint(cadence_max-cadence_min, size=ll)+cadence_min


def fakewave(samplerate,cadence):
#    cadence=cadence/60*360/samplerate #換單位=>度/比
    f_ys=np.zeros(0)
    ll=cadence/60*samplerate
#    print(ll)
    for cad in cadence:
        
        ys=np.arange(-180,180,int(cad))
        f_ys=np.hstack((f_ys,ys))
    return f_ys

ys=fakewave(samplerate,cadence)


from peakdetect import *
maxtab, mintab = peakdet(ys,150)


estimated_f=1/(np.diff(maxtab[:,0])/samplerate)
plt.plot(cadence[1:-2],label='input_f')
print(len(cadence[:len(estimated_f)]),len(np.hstack((np.zeros(1),estimated_f))))
plt.plot(estimated_f,label='output_f')
plt.legend()
plt.show()





xs=np.linspace(0,len(ys)/samplerate,len(ys))
plt.plot(xs,ys)
plt.xlabel('ts')
plt.ylabel('degree')
plt.show()






#s=Signal(ys.reshape([len(ys),1]))
#s.movingavg(0.3,0.01,100,[0])
#def detectcadence(ys,window,samplerate):
#    cadence=np.zeros_like(ys)
##    temp=[np.mean(ys[x-window:x+window]) for x in range(window,len(ys)-window)]
#    temp=ys
#    buffer=[]
#    buffersize=10
#    px=[]
#    for i in range(len(temp)):
#        if len(buffer)<window:
#            buffer.append(temp[i])
#        else:
#            buffer.remove(buffer[0])
#            buffer.append(temp[i])
#            
#        if len(buffer)==window:
#            if max(buffer)>350:
#                if buffer.index(max(buffer))<buffersize or buffer.index(max(buffer))>0:
#                    px.append(i)
#        
#    return temp,px
#window=5
#temp,px=detectcadence(ys,window,samplerate)
#plt.plot(np.linspace(0,len(temp)*(1/samplerate),len(temp)),temp)
#
#plt.plot(xs,ys)
#
#px=np.array(px)*(1/samplerate)
#py=np.ones_like(px)*400
#plt.scatter(px,py)

#wx=np.linspace(0,len(temp)*(1/samplerate),len(temp))
#wy=temp

#plt.plot(xs[:600],ys[:600])



#a=[1,2,3,4,9,5]
#
#a.index(9)
#def fakewave(xs,cadence,samplerate,noisy,farray):
#    cadence=cadence/60*360 #換單位=>度/s
##    ys=np.ones_like(xs)*cadence*(1/samplerate)
##    ys=np.cumsum(ys)
#    ys=np.zeros_like(xs)
#    f_ys=np.zeros(0)
#    print(farray)
#    for f in farray:
#        print(f)
#        for i in range(0,len(ys)):
#            temp=0
#            for k in range(0,noisy):
#                temp+=(-1)**(k+1)*np.sin(2*np.pi*(k+1)*f*xs[i])/(k+1)
#            ys[i]=temp*2/np.pi*360
#        f_ys=np.hstack((f_ys,ys))
#        plt.plot(f_ys)
#        plt.show()
##        f_ys=np.hstack((ys))
##    ys=np.cumsum(ys)*2/np.pi
#    return f_ys
#
#xs=np.linspace(0,duration,duration*samplerate)