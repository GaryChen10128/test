# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:22:22 2019

@author: 180218
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
v0=np.array([0,1]).reshape(2,1)
delta_alpha=10/180*np.pi
end_alpha=360/180*np.pi
R=np.array([[np.cos(delta_alpha),-np.sin(delta_alpha)],[np.sin(delta_alpha),np.cos(delta_alpha)]])
v=[]
v.append(v0)
tanget_v=[]

R_t=R
tanget_v.append(R_t.dot(v[-1]))
tanget_p=[]
F=-50
F_list=[]
F_list.append(0)
l_list=[]
ss=0
print('{} {} {} {}'.format('曲柄角度','F與Ft夾角','切線向量算Ft','曲柄角度算Ft'))

for alpha in np.arange(0,end_alpha,delta_alpha):
    #position vector
    plt.scatter(v[-1][0],v[-1][1])
    plt.plot([0,v[-1][0]],[0,v[-1][1]])
    
    #tanget vector
    plt.plot([v[-1][0],tanget_v[-1][0]],[v[-1][1],tanget_v[-1][1]],c='black')

    x1=v[-1][0]
    x2=tanget_v[-1][0]
    y1=v[-1][1]
    y2=tanget_v[-1][1]
    temp_tanget=np.array([x2-x1,y2-y1]).reshape(2,1)
    
    temp_tanget/=norm(temp_tanget)
    tanget_p.append(temp_tanget)
    

    theta=np.arccos(tanget_p[-1][1])  #因為定義為方向逆時針是正 前進速度
    print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(alpha/np.pi*180,(theta/np.pi*180)[0],(F*np.cos(theta))[0],(F*np.sin(-alpha))))
    
    v.append(R.dot(v[-1]))
    tanget_v.append(R_t.dot(v[-1]))

a=np.arange(0,100)
