# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:06:10 2019

@author: 180218
"""

from temp_package import *
import numpy as np
import matplotlib.pyplot as plt

#比對swift跟小黑盒計算結果
Reader.figure(path='./esti_cad.csv')
esti_raw=Reader.export()
temp=np.append(np.zeros(1),np.diff(esti_raw[:,0]))
mk=temp!=0

esti_raw=esti_raw[mk,:]
estk_ts=esti_raw[:,0]
esti_ts=esti_raw[:,0]/1000
esti_tt=esti_raw[-1,0]/1000
esti_samplerate=len(esti_raw)/esti_tt
#esti_ts=np.linspace(0,esti_tt,len(esti_raw))
plt.plot(esti_ts,esti_raw[:,10])




Reader.clr()
Reader.figure(path='./ref_cad.csv')
ref_cad=Reader.export().flatten()
ref_cad=np.append(np.zeros(14),ref_cad) #shit wave to fit time
#ref_samplerate=152/len(ref_cad)
#ref_ts=np.linspace(0,esti_tt,len(ref_cad))
plt.plot(ref_cad)
plt.title('Comparision of ZWIFT and black-box')

plt.ylabel('cadence (RPM)')
plt.xlabel('ts')
plt.show()


#測試app收取小黑盒取樣率變化
samplerate_stack=[]
for i in range(0,len(esti_raw),50):
    try:
        samplerate_stack.append(100/((esti_raw[i+100,0]-esti_raw[i,0])/1000))
    except:
        print('end')
esti_samplerate_ts=np.arange(0,esti_raw[-1,0],len(samplerate_stack))        
plt.plot(samplerate_stack)
plt.xlabel('n')
plt.ylabel('samplerate')
plt.show()


#結果
#大部分曲線穩和，剛開始沒對上可能是zwift有將結果平滑化
#小黑盒取樣率變化大，這樣會使踏頻誤差變大

#討論
#小黑盒使用app時間對的比較上，應該是實際上是穩的，只是跟真實有差一點，但是是在+-範圍內



