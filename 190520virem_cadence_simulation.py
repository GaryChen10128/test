# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:59:50 2019

@author: 180218
"""

from temp_package import *




#func
#def update(temp):
#    angle=temp[:,8]
#    ts=temp[:,2]
#    cad=(max(angle)-min(angle))/sum(ts)/360*60
#    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
#        temp=min(angle[angle>0])-max(angle[angle<0])
##        if temp>200:
#        cad=(360-min(angle[angle>0])+max(angle[angle<0]))/sum(ts)/360*60
#
#    cadence.append(cad)
# 抓最大跟最小
#def update(temp):
#    angle=temp[:,8]
#    ts=temp[:,2]
#    end=angle.argmax()
#    start=angle.argmin()
#    cum_ts=sum(ts[start:end])
#    cad=(max(angle)-min(angle))/cum_ts/360*60
#    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
#        temp=min(angle[angle>0])-max(angle[angle<0])
##        if temp>200:
#        cad=(360-min(angle[angle>0])+max(angle[angle<0]))/sum(ts)/360*60
#    cadence.append(cad)
#    抓頭跟尾
def update(temp):
    angle=temp[:,8]
    ts=temp[:,2]
    cum_ts=sum(ts)
    cad=abs(angle[-1]-angle[0])/cum_ts/360*60
    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
        if(angle[-1]<-90):
            cad=(360-angle[0]+angle[-1])/cum_ts/360*60
        else:
            cad=(abs(angle[0])+angle[-1])/cum_ts/360*60
        cross360_temp=50
    else:
        cross360_temp=0
    cadence.append(cad)
    cross360.append(cross360_temp)
def update0523_bk(temp): #原本以為不應該頭減尾 但是
    angle=temp[:,8]
    ts=temp[:,2]
    cum_ts=sum(ts)
    cad=abs(angle[-1]-angle[0])/cum_ts/360*60
    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
        if(angle[-1]<-90):
            cad=(360-angle[0]+angle[-1])/cum_ts/360*60
        else:
            cad=(abs(angle[0])+angle[-1])/cum_ts/360*60
    cadence.append(cad)    
def update_movavg(temp):
    angle=temp[:,8]
    ts=temp[:,2]
    cum_ts=sum(ts)
    cad=abs(angle[-1]-angle[0])/cum_ts/360*60
    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
        if(angle[-1]<-90):
            cad=(360-angle[0]+angle[-1])/cum_ts/360*60
        else:
            cad=(abs(angle[0])+angle[-1])/cum_ts/360*60
    cadence.append(cad)    
#def update(temp):
#    angle=temp[:,8]
#    ts=temp[:,2]
#    cad=abs(angle[-1]-angle[0])/sum(ts)/360*60
#    if(len(angle[angle>0])>0)and(len(angle[angle<0])>0):
##        temp=min(angle[angle>0])-max(angle[angle<0])
#        
##        if temp>200:
#            cad=(360-min(angle[angle>0])+max(angle[angle<0]))/sum(ts)/360*60
#
#    cadence.append(cad)    

if __name__=='__main__':
    #para
    cadence=[]
    cross360=[]
#    Reader.figure(path="D:/iii/exp_data/vierm_app/gg.csv",header=0)
#    raw=Reader.export()
#    raw=raw[1600:]
#    eu_angle=raw[:,7]
#    delt_ts=raw[:,1]
    Reader.figure(path="D:/iii/exp_data/vierm_app/gg3.csv",header=0)
    raw=Reader.export()
    ref=raw[raw[:,0]==1]
    ref_cad=ref[:,1]
    raw=raw[raw[:,0]==0]
    app_cadence=raw[:,7]
    
    windowsize=5
    mov_eu=[]
    for i in range(len(raw)-windowsize):
        window=raw[i:i+windowsize]
        avg=np.average(window[:,8])
        mov_eu.append(avg)
    mov_eu=np.array(mov_eu)
    mov_ts=np.cumsum(raw[:-windowsize,2])
    mov_raw=np.zeros([len(mov_eu),10])
    mov_raw[:,2]=raw[:-windowsize,2]
    mov_raw[:,8]=mov_eu
    
    plt.show()
    plt.title('moving_raw')
    plt.plot(np.cumsum(raw[:,2]),raw[:,8])
    plt.plot(mov_ts,mov_eu)
    plt.show()

    eu_angle=raw[:,8]
    delt_ts=raw[:,2]
    
    
#moving avg
    cad_window=10
    for i in range(len(eu_angle)-cad_window):
        window=raw[i:i+cad_window]
        update(window)
#    for i in range(len(mov_raw)-cad_window):
#        window=mov_raw[i:i+cad_window]
#        update(window)        
        
#    plt.ylim(0,60)

    plt.title('cad algo implement on app') 
    plt.plot(app_cadence)
    plt.show()


    plt.title('cad algo implement on python');
#    plt.ylim(0,60)
    plt.plot(cadence)
    plt.show()
#    plt.plot(app_cadence)
    plt.title('cad algo implement on ishape')
    plt.plot(ref_cad)    
    plt.show()
#buffer for calculate cadence
    mov_cad=Signal(np.array(cadence).reshape(len(cadence),1))
    mov_cad.movingavg(window_s=1,shift_s=0.3,samplerate=31,index=[0],title='',starttime=0,save=True,show_detail=False,showfig=False)
    plt.title('py-algo after movavg')
    plt.plot(mov_cad.moving_avg.values)
    plt.show()
    
    plt.title('hyposis')
    plt.plot(cadence)
    plt.plot(cross360)
    plt.show()
#    mov_cad=Signal(np.array(app_cadence).reshape(len(app_cadence),1))
#    mov_cad.movingavg(window_s=2,shift_s=0.3,samplerate=31,index=[0],title='',starttime=0,save=True,show_detail=False,showfig=True)
#    plt.plot(mov_cad.moving_avg.values*3)


#    plt.plot(raw[:,6])
