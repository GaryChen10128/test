# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:44:18 2019

@author: 180218
"""

from sql import SQLite,Table
from temp_package import *
import matplotlib.pyplot as plt
body_table=['head','c3','t3','t7','rs','0','c7','ls']
dev_name=['head','c7','t3','ls','rs'] #rs
if (dev_name[0]=='ls' or dev_name[0]=='rs'):
    aim=2
else:
    aim=0
beta=0.5
#start
date='190121'
#date='without_remind'
#
if __name__=='__main__':
    db=SQLite(path='./crom_imu_compare.db')
    tablelist=np.array(db.get_table(),dtype='str')
    for a in tablelist:
        print(a)
    
    for talbelist_item in tablelist:        
        
        try:

            subject=0
            session=0
            head=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0],tablename=talbelist_item)
            dev01=IMU(head,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
            dev01.calc_angle(fake_t_on=True)
            #dev01.to_qeb(50,51)
            dev01.show_eu()
            c7=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[1],tablename=talbelist_item)
            dev02=IMU(c7,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
            dev02.calc_angle(fake_t_on=True)
        #    dev01.to_qeb(50,51)
            dev02.show_eu()    

            t3=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[2],tablename=talbelist_item)
            dev03=IMU(t3,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
            dev03.calc_angle(fake_t_on=True)
        #    dev01.to_qeb(50,51)
            dev03.show_eu()     

            test1=Connector(dev01,dev02)
            test2=Connector(dev01,dev03)
            test1.get_angle_minus()
            test2.get_angle_minus()

            test1.plt_angle(index=[aim])
            index=[0]
            test=copy.deepcopy(dev01.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_self')


            test.moving_avg.peak_green(title=talbelist_item+'_self',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(test.moving_avg.out_a,-test.moving_avg.out_b)
            Writer.appendfile(out,keys=[talbelist_item,'self',str(index[0])])

            index=[1]
            test=copy.deepcopy(dev01.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_self')


            test.moving_avg.peak_green(title=talbelist_item+'_self',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'self',str(index[0])])    
            index=[2]
            test=copy.deepcopy(dev01.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_self')


            test.moving_avg.peak_green(title=talbelist_item+'_self',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(test.moving_avg.out_a,-test.moving_avg.out_b)
            Writer.appendfile(out,keys=[talbelist_item,'self',str(index[0])])
            test1.plt_angle(index=[aim])
            test2.plt_angle(index=[aim])
            index=[0]
            test=copy.deepcopy(test1.imu1_body.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_c7')


            test.moving_avg.peak_green(title=talbelist_item+'_c7',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(test.moving_avg.out_a,-test.moving_avg.out_b)
            Writer.appendfile(out,keys=[talbelist_item,'c7',str(index[0])])
            index=[1]
            test=copy.deepcopy(test1.imu1_body.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_c7')


            test.moving_avg.peak_green(title=talbelist_item+'_c7',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'c7',str(index[0])])
            index=[0]
            test=copy.deepcopy(test2.imu1_body.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_t3')


            test.moving_avg.peak_green(title=talbelist_item+'_t3',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(test.moving_avg.out_a,-test.moving_avg.out_b)
            Writer.appendfile(out,keys=[talbelist_item,'t3',str(index[0])])
            index=[1]
            test=copy.deepcopy(test2.imu1_body.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_t3')


            test.moving_avg.peak_green(title=talbelist_item+'_t3',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'t3',str(index[0])])
            test1.show_eu()
            test1.show_eu(index=[0])
            test1.autoadg_by_gyr()
            test1.rotatebackrate_dynamic()
            test1.show_eu(index=[2])
            test2.show_eu()
            test2.show_eu(index=[0])
            test2.autoadg_by_gyr()
            test2.rotatebackrate_dynamic()
            test2.show_eu(index=[2])
            index=[2]
            test=copy.deepcopy(test1.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_c7')


            test.moving_avg.peak_green(title=talbelist_item+'_c7',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'c7',str(index[0])])
            index=[2]
            test=copy.deepcopy(test2.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_t3')


            test.moving_avg.peak_green(title=talbelist_item+'_t3',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'t3',str(index[0])])
            dev01.show_eu()
            dev01.show_eu(index=[0])
            dev01.autoadg_by_gyr()
            dev01.rotatebackrate_dynamic()
            dev01.show_eu(index=[2])
            index=[2]
            test=copy.deepcopy(dev01.eu)
            test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=talbelist_item+'_self')


            test.moving_avg.peak_green(title=talbelist_item+'_self',tag=str(index[0]))
            Writer.figure(path="./out.csv",)
            out=np.append(-test.moving_avg.out_b,test.moving_avg.out_a)
            Writer.appendfile(out,keys=[talbelist_item,'self',str(index[0])])
        except:
            Writer.figure(path="./error.csv",)
            Writer.appendfile(np.zeros(6),keys=[talbelist_item,'self',str(index[0])])