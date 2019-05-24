# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:26:44 2019

@author: 180218
"""

from temp_package import *
import matplotlib.pyplot as plt
import numpy as np


adp=Adaptor(date='190423-3',subject=0,session=0,raw_or_cali=None)
baby=SafePlay(adp)
l_imu,r_imu,l_press,r_press=baby.get_data()

r_imu.show_raw()
r_imu.calc_angle(fake_t_on=False)
l_imu.calc_angle(fake_t_on=False)
r_imu.show_eu()


index=[0]
test=r_imu.eu
#temp_test=r_press[:,-1].reshape(len(r_press),1)
#test=Signal(temp_test)
#test.movingavg(window_s=0.5,shift_s=0.25,samplerate=12,index=[0],title=l_imu.table+'_self')
#test.moving_avg.peak_cadence(title=l_imu.table+'_self',tag=str(index[0]))
#t1=test.moving_avg
test=test.smoothListGaussian(index=index[0])
test.peak_cadence(title=r_imu.table+'_self',tag=str(index[0]))
t1=test
#t1.dt
#delt=t1.dt[:,0]
delt=t1.dt_max
#plt.figure(3)
rpm=(delt*0.083/60)
for i in range(len(rpm)):
    rpm[i]=1/rpm[i]
dt_max_ts=r_imu.ts.values[t1.dt_max_ts.tolist()]

plt.plot(dt_max_ts[:-1],rpm,label='maxtab')
delt=t1.dt_min
rpm=(delt*0.083/60)
for i in range(len(rpm)):
    rpm[i]=1/rpm[i]

plt.grid()
plt.ylabel('cadence')
dt_min_ts=r_imu.ts.values[t1.dt_min_ts.tolist()]
plt.plot(dt_min_ts[:-1],rpm,label='mintab')  



#Reader.figure(path='D:/iii/exp_data/safeplay/20190423165030.csv')
Reader.figure(path='D:/iii/exp_data/safeplay/20190423181219.csv')
#Reader.figure(path='D:/iii/exp_data/safeplay/20190425113604.csv',shape=[10000,5])
#Reader.figure(path='D:/iii/exp_data/safeplay/20190425160949.csv')
plt.plot(np.diff(raw[:,-1]))
raw=Reader.export()
crank_ts=raw[:,0]/1000
samplerate=len(crank_ts)/crank_ts[-1]
plt.plot(crank_ts)
plt.plot(np.diff(crank_ts))
cad=raw[:,-2]
plt.ylim([0,200])
plt.plot(crank_ts-23,cad,label='black box')
plt.legend()
plt.xlabel('ts')

rate=raw[:,-1]
rp_p=r_press[:,-1]
rp_ts=r_press[:,1]
index=np.searchsorted(crank_ts,rp_ts)
rp_rate=rate[index]
plt.plot(raw[:,0])
rp_rate_ts=raw[index,0]
plt.plot(rp_rate_ts,rp_rate)
rp_power=rp_p*rp_rate

#len(rpm)
#len(t1.dt_max_ts)
#len(t1.dt_min_ts)
#t1.dt_min_ts[0]

#
#l_imu.samplerate
#
#
#plt.plot(l_press[:,-1])
#plt.plot(r_press[:,-1])
#
#plt.plot(l_press[2950:3000,1],l_press[2950:3000,-1],label='left')
#plt.plot(r_press[2950:3000,1],r_press[2950:3000,-1],label='right')
##plt.plot(l_press[3550:3600,-1],label='left')
##plt.plot(r_press[3550:3600,-1],label='right')
#
##plt.plot(l_press[2950:3000,-1],label='left')
##plt.plot(r_press[2950:3000,-1],label='right')
##plt.plot(l_press[3550:3600,-1],label='left')
##plt.plot(r_press[3550:3600,-1],label='right')
#plt.legend()
#plt.grid()
#def smoothListGaussian(listin,strippedXs=False,degree=5):  
#    window=degree*2-1  
#    weight=np.array([1.0]*window)  
#    weightGauss=[]  
#    for i in range(window):  
#        i=i-degree+1  
#        frac=i/float(window)  
#        gauss=1/(np.exp((4*(frac))**2))  
#        weightGauss.append(gauss)
#    weight=np.array(weightGauss)*weight  
#    smoothed=[0.0]*(len(listin)-window)  
#    for i in range(len(smoothed)):        smoothed[i]=sum(np.array(listin[i:i+window])*weight)/sum(weight)  
#    return smoothed
#x=l_press[:,1]
#y=l_press[:,-1]
#x = smoothListGaussian(x)
#y = smoothListGaussian(y)
#x2=r_press[:,1]
#y2=r_press[:,-1]
#x2 = smoothListGaussian(x2)
#y2 = smoothListGaussian(y2)
#
##start=3300
#end=3600
#plt.plot(x[start:end],y[start:end],label='left')
#plt.plot(x[start:end],y[start:end],label='left')
#
#plt.plot(x2[start:end],y2[start:end],label='right')
##plt.plot(r_press[3550:3600,-1],label='right')
#plt.legend()
#plt.grid()
#

#x=np.linspace(-360/180*np.pi,0/180*np.pi,1000)
#print(x.shape)
#x=np.tile(x,5)
#print(x.shape)
#y=np.sin(x)
#plt.plot(y)

#a=np.array([1,2,3])
#u=np.repeat(a,3,axis=1)
#u

len(crank_ts)/crank_ts[-1]
adp=QuickAdp(data=raw)
imu1.samplerate
imu1=IMU(adp,mag_on=False,beta=1,mag_cali_on=False,acc_cali_on=False)
#imu1.acc.changeorder([-3,1,2])
#imu1.gyr.changeorder([3,-1,-2])
imu1.calc_angle(fake_t_on=False)
imu1.samplerate
imu1.show_eu()
