# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:26:44 2019

@author: 180218
"""
from temp_package import *
import matplotlib.pyplot as plt
import numpy as np
beta=1
Reader.figure(path='./raw/190401balance/20190329174639.csv')
raw=Reader.export()
adp=QuickAdp(data=raw)

imu1=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
imu1.calc_angle(fake_t_on=True)
imu1.samplerate
imu1.show_eu()

imu1.to_qeb(1,2)
#plt.plot(imu1.ts.values[:10*90],imu1.eu.values[:10*90])


#imu1.show_raw()




x=imu1.eu.values[:,0]
y=imu1.eu.values[:,1]
mk1=(y-x)>0
n_mk1=np.logical_not(mk1)
mk2=(y+x)>0
n_mk2=np.logical_not(mk2)
mk11=np.logical_and(mk1,mk2) #3
mk22=np.logical_and(n_mk1,mk2) #2
mk33=np.logical_and(n_mk1,n_mk2) #1
mk44=np.logical_and(mk1,n_mk2) #4
mk=mk44
#plt.scatter(imu1.eu.values[mk,0],-imu1.eu.values[mk,1])
#plt.grid()
#plt.xlim(-20,20)
#plt.ylim(-20,20)
#plt.xlabel('left -> right')
#plt.ylabel('backword -> forward')

Writer.figure(path='./g2g.csv',automode=False)
#for i in range(len(imu1.eu.values)):
#    Writer.appendfile(imu1.eu.values[i])
#Writer.close()
t=imu1.ts.values*1000
s1=np.ones_like(imu1.ts.values)
s1[mk11]=3
s1[mk22]=2
s1[mk33]=1
s1[mk44]=4




t_eu=imu1.eu.values[::100,0]
t_eu2=-imu1.eu.values[::100,1]
t_s1=s1[::100]
plt.scatter(t_eu,t_eu2,c=t_s1)
plt.vlines(0,-20,20)
plt.hlines(0,-20,20)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.grid()
plt.xlabel('left -> right')
plt.ylabel('backword -> forward')



esti_t=imu1.ts.values*1000
esti_stage=s1




Reader.clr()
Reader.figure(path='./raw/190401balance/righttimeandXY.csv')
fit=Reader.export()
ref_t=fit[:,0]

f_t=np.searchsorted(esti_t,ref_t)
fit_stage=[]
for i in f_t.tolist():
    if i!=len(esti_stage):
        fit_stage.append(esti_stage[i])
    else:
        fit_stage.append(esti_stage[-1])
y=np.array(fit_stage,dtype=int)
plt.plot(y)




from animator import *
#x = np.linspace(-3, 3, 91)
#t = np.linspace(0, 25, 90)
#y = np.linspace(-3, 3, 91)
#FF=
#ani=Animator(animation_type='scatter')
#
#FF=
x=t_eu.reshape(len(t_eu),1)
##y=t_eu2
f=t_eu2.reshape(len(t_eu2),1)
f2=np.hstack((x,f))
#ani=Animator(x=x,y=y,t=t,animation_type='scatter',FF=f2)
#ani=Animator(x=x,y=x,t=x,animation_type='scatter',FF=f2,interval=200)
ani=Animator(data=f2,animation_type='scatter',interval=100)
#ani.start()

#x=118
#plt.scatter(x,y)

