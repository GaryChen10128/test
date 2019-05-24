# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:06:10 2019

@author: 180218
"""

from temp_package import *
import numpy as np
import matplotlib.pyplot as plt

#比對swift跟小黑盒計算結果
#Reader.figure(path='./123.csv',header=1,shape=[20000,9])
Reader.figure(path='./sub_b1.csv',header=1,shape=[20000,9])
#Reader.figure(path='./sub_b2.csv',header=1,shape=[20000,9])


esti_raw=Reader.export()


temp=np.append(np.zeros(1),np.diff(esti_raw[:,3]))
mk=temp!=0



ts=Reader.timeanalysis(1)
ts=ts[mk,:]

ts=np.array(ts,dtype='int')
ts2=ts[:,3]*3600+ts[:,4]*60+ts[:,5]+ts[:,6]/1000
diff_t=np.diff(ts2)


#plt.xlim(10000,10300)
plt.plot(1/diff_t)
plt.show()
plt.plot(1/diff_t[::-1])
plt.show()

plt.plot(1/diff_t[:10*3600])
plt.show()
np.mean(1/diff_t[:10*3600])
#ts=self.df.iloc[start:end,0].str.replace('-',' ').str.split(' ',expand=True).applymap(lambda x: int(x, 16)).as_matrix()


