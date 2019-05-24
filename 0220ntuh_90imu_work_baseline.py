from temp_package import *
import matplotlib.pyplot as plt
body_table=['head','c3','t4','t7','rs','0','c7','ls']
dev_name=['head','c7'] #rs
if (dev_name[0]=='ls' or dev_name[0]=='rs'):
    aim=2
else:
    aim=0
beta=0.5
#start
#date='remind'
#date='without_remind'
#
date='ntuh_work_baseline'
sub=21
session=2
testmode=True

for i in range(sub,sub+1): #0-14
    subject=i
    head=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0],testmode=testmode)
    dev01=IMU(head,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
#    break
    plt.plot(dev01.delta_ts.values,label='delta_ts')
    
    x=dev01.delta_ts.values
    plt.legend()
    plt.show()  
    dev01.calc_angle(fake_t_on=True)
#    dev01.show_eu()
#    dev01.to_qeb(start=40,end=50)
    dev01.show_eu(index=[aim])
    
    
  
    C7=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[1],testmode=testmode)
    dev02=IMU(C7,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
    dev02.calc_angle(fake_t_on=True)
#    dev02.to_qeb(start=40,end=50)
    dev02.show_eu(index=[aim])
    
#    c4=IMU(C7,mag_on=True,beta=beta,mag_cali_on=True,acc_cali_on=False)
#    c4.calc_angle(fake_t_on=True)
#    c4.to_qeb(start=20,end=30)
#    c4.show_eu(index=[aim])
    
  
    
    head_body=Connector(dev01,dev02)
    head_body.get_angle_minus()

    head_body.plt_angle(index=[aim])
    plt.show()
    plt.title(dev01.file_tag+'_trim')
    plt.plot(head_body.imu1_body.ts.values[0:9*31*60],head_body.imu1_body.eu.values[0:9*31*60,0])
    plt.show()
    print('duration',int(head.bias[i-1])/60)

    
    head_body.cali_angle_zero(start=100,end=110)
    
    
