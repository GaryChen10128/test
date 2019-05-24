# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:26:44 2019

@author: 180218
"""
from temp_package import *
import matplotlib.pyplot as plt
import numpy as np


beta=1

#path='./raw/190408balance/tester02.csv'
path='./raw/190408balance/tester01.csv'

Reader.figure(path=path)
raw=Reader.export()
adp=QuickAdp(data=raw)

imu1=IMU(adp,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
imu1.calc_angle(fake_t_on=True)
imu1.samplerate
imu1.show_eu()
plt.figure(2)
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
#t_s1=s1[::]
#t_eu=imu1.eu.values[::,0]
#t_eu2=-imu1.eu.values[::,1]
#
#plt.plot(t_eu,t_eu2)
plt.scatter(t_eu,t_eu2,c=t_s1)
plt.vlines(0,-20,20)
plt.hlines(0,-20,20)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.grid()
plt.xlabel('left -> right')
plt.ylabel('backword -> forward')
plt.show()


esti_t=imu1.ts.values*1000
esti_stage=s1




#Reader.clr()
##path='./raw/190401balance/righttimeandXY.csv'
##path='./raw/190408balance/Left_tester01.csv'
##path='./raw/190408balance/Left_tester02.csv'
##path='./raw/190408balance/Right_tester01.csv'
#path='./raw/190408balance/Right_tester02.csv'
#Reader.figure(path=path,header=0)
#fit=Reader.export()
#ref_t=fit[:,0]
#
#f_t=np.searchsorted(esti_t,ref_t)
#fit_stage=[]
#for i in f_t.tolist():
#    if i!=len(esti_stage):
#        fit_stage.append(esti_stage[i])
#    else:
#        fit_stage.append(esti_stage[-1])
#y=np.array(fit_stage,dtype=int)
#plt.plot(y)
#



from animator import *

x=t_eu.reshape(len(t_eu),1)
f=t_eu2.reshape(len(t_eu2),1)
data=np.hstack((x,f))


d2=np.expand_dims(data, axis=2)
d2=np.zeros([len(data),2,1])

d2[:,:,0]=data
#d2[:,:,1]=data-data/2
#d2[:,:,2]=data-data/2-data/4
ani=Animator(data=d2,animation_type='scatter',interval=100)
#ani=Animator(data=d2,animation_type='vector',interval=100)


#plt.plot(d2[:2,0,0], d2[:2,1,0])
#d2[0,:,0]
#d2[5,:,1]
#d2[0,1,0]
#d2[0,1,1]
#plt.scatter(d2[0,0,:], d2[0,1,:])
#d2[0,:,:]
#d2[0,:,0]
#d2[0,0,:]
#d2[0,1,:]
#scats=np.zeros(3,dtype=object)
#(scats[2])?
#scats?
#plt.quiver([3,3],[5,5])
#plt.quiver([5],[5])
#plt.quiver([3,4],[3,4],[1,5],[3,5])

#
#x = np.linspace(0,1,11)
#y = np.linspace(1,0,11)
#u=plt.plot(x,y)
#u.set_ydata(5)
#u = v = np.zeros((11,11))
#u[5,5] = 0.2
#
#plt.axis('equal')
#plt.quiver(x, y, u, v, scale=1, units='xy')
#


#x = np.arange(-3, 3, 0.01)
#j = 1
#y = np.sin( np.pi*x*j ) / ( np.pi*x*j )
#fig = plt.figure()
#ax = fig.add_subplot(111)
##plot a line along points x,y
#line, = ax.plot(x, y)
##update data
#j = 2
#y2 = np.sin( np.pi*x*j ) / ( np.pi*x*j )
##update the line with the new data
##line.set_ydata(y2)
#
#plt.show()