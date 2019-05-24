from temp_package import *
import matplotlib.pyplot as plt
body_table=['head','c3','t4','t7','rs','0','c7','ls']
dev_name=['head','c7'] #rs
if (dev_name[0]=='ls' or dev_name[0]=='rs'):
    aim=2
else:
    aim=0
beta=1
#start
#date='remind'
#date='without_remind'
#
date='190307'
sub=1
session=1
testmode=True
dehead_time=0
manualinputbias=-25.45

for i in range(sub,sub+1): #0-14
    subject=i
    head=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0],testmode=testmode)
    dev01=IMU(head,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
#    break
#    dev01.show_raw()
#    plt.plot(dev01.ts.values)
    dev01.calc_angle(fake_t_on=False)
#    dev01.show_raw()
#    plt.plot(head.acc.values[:,0],label='x')
#    plt.plot(head.acc.values[:,1],label='y')
#    plt.plot(head.acc.values[:,2],label='z')
#    plt.legend()
#    plt.show()
    plt.plot(head.delta_ts.values,label='delta_ts')
    plt.xlabel('n')
    plt.ylabel('delta_t')
    plt.legend()
    plt.show()    
#    dev01.show_eu(index=[aim])
#    plt.plot(dev01.ts.values,dev01.eu.values)
#    dev01.to_qeb(start=40,end=50)

#    break
#    dev01.show_eu(index=[aim])
#    break
    C7=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[1],testmode=testmode)
    dev02=IMU(C7,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
    dev02.calc_angle(fake_t_on=True)
#    dev02.to_qeb(start=40,end=50)
#    plt.plot(C7.acc.values[:,0],label='x')
#    plt.plot(C7.acc.values[:,1],label='y')
#    plt.plot(C7.acc.values[:,2],label='z')
#    plt.legend()
#    plt.show()
    dev02.show_eu(index=[aim])
    
#    c4=IMU(C7,mag_on=True,beta=beta,mag_cali_on=True,acc_cali_on=False)
#    c4.calc_angle(fake_t_on=True)
#    c4.to_qeb(start=20,end=30)
#    c4.show_eu(index=[aim])
    
  
    
    head_body=Connector(dev01,dev02)
#    head_body.dehead(duration=head.bias[i-1])
#    head_body.imu1.dehead(start=int(head.bias[i-1]))
#    head_body.imu1.acc.norm().plot_ts(index=[0])
#    head_body.show_eu(index=[aim])
#    head_body.eu.feature_analysis2(window_s=300,shift_s=300,samplerate=dev01.samplerate,remind='withoud_remind',index=0,title=dev01.file_tag+'_angle',starttime=dev01.ts.values[0],save=True)

#    head_body.get_angle_minus()

    head_body.plt_angle(index=[aim])
#    plt.show()
#    plt.title(dev01.file_tag+'_trim')
#    plt.plot(head_body.imu1_body.ts.values[0:9*31*60],head_body.imu1_body.eu.values[0:9*31*60,0])
#    plt.show()
#    print('duration',int(head.bias[i-1])/60)

    
#    head_body.cali_angle_zero(start=10,end=12,manual=manualinputbias)
    
#    angleslap=head_body.zeros
    head_body.plt_angle(index=[aim])
    
    head_body.eu=head_body.imu1_body.eu
    head_body.qq=head_body.imu1_body.qq
#    head_body.dehead(duration=dehead_time)
    head_body.eu.feature_analysis2(window_s=300,shift_s=300,remind='without_remind',index=0,samplerate=dev01.samplerate,title=dev01.file_tag+'_angle',starttime=dev01.ts.values[0],save=True)

#190307stop
#plt.plot(1/np.diff(head.ts.values))
#plt.ylim(25,35)
#plt.plot(np.diff(head.ts.values)*1000)
#x=np.diff(head.ts.values)*1000

#    head_body.plt_angle(index=[aim])
#    break
#    tt=2450
#    threshold=5
#    head_body.eu.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[aim],title=dev01.file_tag)
#    head_body.eu.moving_avg.trim(ts=tt).show_peak(samplerate=1,distance=170,threshold=threshold)
 
    #-----test use moving result peak
#    test=head_body.eu.abs_sig
#    test.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[aim],title=dev01.file_tag)
#    test.moving_avg.trim(ts=tt).show_peak(samplerate=1,distance=120,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x
#    head_body.eu.moving_avg.trim(ts=tt).plot_ts(tag=temp_tag,index=[0])

#    break
    




#
#------------------expoert data to csv-----------------------
def outdata(data,samplerate,title,remind,index):
    mean=[]
    std=[]
    median=[]
    for i in range(0,len(data),300*samplerate):
#        print(i)
        
        temp=data[i:i+300*samplerate,0]
        if remind=='remind':
            
            if i==5*300*samplerate or i==12*300*samplerate:
                temp=temp[:-(samplerate*60)]
    #            temp=np.ones_like(temp)*90
            if i==6*300*samplerate or i==13*300*samplerate:
                temp=temp[(samplerate*90):]    
#            temp=np.ones_like(temp)*90
        print(len(temp))
        try:
            mean.append(np.mean(temp,axis=0))
            std.append(np.std(temp,axis=0))
            median.append(np.median(temp,axis=0))
        except:
            continue
    mean,std,median=np.array(mean),np.array(std),np.array(median)   
    out=np.vstack((mean,std,median))
    excel=out.transpose()
    raw=data
    mv=Signal(raw)
    mv.movingavg(20,12,samplerate,index=index,title='movingavg')
    moving_raw=np.array(mv.after_moving)
    fig, (ax0) = plt.subplots(nrows=1, sharex=True)
    ax0.set_title(title)
    ax0.set_ylabel('degree')
    ax0.set_xticks(np.arange(1,1+len(mean),1))
    ax0.grid()
    ax0.errorbar(np.linspace(1,len(mean),len(mean)), mean, std, fmt='-o')
    fig.savefig('./output/'+title+'.png')
    return np.vstack((mean,std,median)),excel,raw[:,0],moving_raw
#190307stop
out,out1,out2,out3=outdata(head_body.eu.values,samplerate=int(dev01.samplerate),title=dev01.file_tag+'errorbar',remind='without_remind',index=[0])
plt.show()
head_body.imu1.dehead(start=int(head.bias[i-1]))
head_body.imu1.acc.norm().plot_ts(index=[0])
#------------------expoert data to csv-----------------------

