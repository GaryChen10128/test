from temp_package import *
import matplotlib.pyplot as plt

body_table=['head','c3','t4','t7','rs','0','c7','ls']
dev_name=['head','c7','c3','ls','rs'] #rs
if (dev_name[0]=='ls' or dev_name[0]=='rs'):
    aim=2
else:
    aim=0
beta=0.5
date='190201'
#
if __name__=='__main__':
        
    subject=0
    session=1
    head=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0])
    dev01=IMU(head,mag_on=False,beta=beta,mag_cali_on=False,acc_cali_on=False)
    dev01.calc_angle(fake_t_on=True)
#    dev01.to_qeb(50,51)
    dev01.show_eu()
    
    index=[0]
    test=copy.deepcopy(dev01.eu)
    test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=index,title=dev01.file_tag)
    from peakdetect import *
    maxtab, mintab = peakdet(test.moving_avg.values,.5)
    plt.plot(test.moving_avg.values)
    plt.scatter(np.array(maxtab)[:,0], np.array(maxtab)[:,1], color='blue')
    plt.scatter(np.array(mintab)[:,0], np.array(mintab)[:,1], color='red')
    plt.show()
    l=min(len(maxtab),len(mintab))
    diff=maxtab[:l,:]-mintab[:l,:]
    diff[:l,0]=maxtab[:l,0]
    #num of max peak output
    num_peak=6
    index=diff[:,1].argsort()[-num_peak:]
    print(index)
    out=diff[np.sort(index),1]
    print('answer is ',out)
    Writer.figure(path="log.csv",)
    Writer.appendfile(out)

#    test=copy.copy(dev01.eu)
#
#    test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=[1],title=dev01.file_tag)
#
#
#    series=test.moving_avg.values
#    from peakdetect import *
#    maxtab, mintab = peakdet(series,.5)
#    plt.show()
#    plt.plot(series)
#    plt.scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
#    plt.scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
#    plt.show()
#    diff=maxtab[:13]-mintab[:13]





#    test=dev01.eu.abs_sig    
##    test=copy.copy(dev01.eu)
#    threshold=30
#    distance=100
#    test.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[2],title=dev01.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x-5
#    dev01.eu.plot_ts(tag=temp_tag,index=[2])    
    
#    subject=0
#    session=1
#    head2=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0])
#    dev02=IMU(head2,mag_on=True,beta=beta,mag_cali_on=True,acc_cali_on=False)
#    dev02.calc_angle(fake_t_on=True)
#    dev02.to_qeb(12,15)
#    dev02.show_eu()

#    test=dev02.eu.abs_sig
#    test=copy.copy(dev02.eu)
#    threshold=40
#    distance=100
#    test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=[aim],title=dev02.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x
#    dev02.eu.plot_ts(tag=temp_tag[:-2],index=[0])
#    
#    test=dev02.eu.abs_sig
#    test=copy.copy(dev02.eu)
#    threshold=20
#    distance=50
#    test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=[1],title=dev02.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x-2
#    dev02.eu.plot_ts(tag=temp_tag,index=[1])
#
#    series=test.moving_avg.values
#    from peakdetect import *
#    maxtab, mintab = peakdet(series,.5)
#    plot(series)
#    scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
#    scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
#    show()
#    diff=maxtab[:15]-mintab[:15]
#        


#    test=dev02.eu.abs_sig    
#    test=copy.copy(dev02.eu)
#    threshold=30
#    distance=50
#    test.movingavg(window_s=2,shift_s=0.1,samplerate=32,index=[2],title=dev02.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x-5
#    dev02.eu.plot_ts(tag=temp_tag,index=[2])   
#    
#    series=test.moving_avg.values
#    from peakdetect import *
#    maxtab, mintab = peakdet(series,.5)
#    plot(series)
#    scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
#    scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
#    show()
#    diff=maxtab[:15]-mintab[:15]
        
    
    
    
    
    
    
    
    
    
#    from scipy import signal
#    
#    subject=0
#    session=2
#    head3=Adp_aiq(date,subject=subject,session=session,dev_name=dev_name[0])
#    dev03=IMU(head3,mag_on=True,beta=beta,mag_cali_on=True,acc_cali_on=False)
#    dev03.calc_angle(fake_t_on=True)
#    dev03.to_qeb(3,4)
#    dev03.show_eu()
#    dev03.eu.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[aim],title=dev03.file_tag)
#
#
#    peakind = signal.find_peaks_cwt(dev03.eu.moving_avg.values, np.arange(1,18000))
#    plt.plot(dev03.eu.mv_x,dev03.eu.moving_avg.values)
#    peakind, xs[peakind], data[peakind]

#    
#
#    series=dev03.eu.moving_avg.values
#    from peakdetect import *
#    maxtab, mintab = peakdet(series,.5)
#    plot(series)
#    scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
#    scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
#    show()
#    diff=maxtab-mintab

#    dev03.eu.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
    
#    test=dev03.eu.abs_sig
#    test=copy.copy(dev01.eu)
#    threshold=40
#    distance=100
#    test.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[aim],title=dev03.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x
#    dev03.eu.plot_ts(tag=temp_tag[:],index=[0])
#    
#    test=dev02.eu.abs_sig
#    test=copy.copy(dev02.eu)
#    threshold=20
#    distance=50
#    test.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[1],title=dev02.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x-2
#    dev02.eu.plot_ts(tag=temp_tag,index=[1])

#    test=dev02.eu.abs_sig    
#    test=copy.copy(dev01.eu)
#    threshold=30
#    distance=50
#    test.movingavg(window_s=4,shift_s=0.1,samplerate=32,index=[2],title=dev02.file_tag)
#    test.moving_avg.trim(ts=-1).show_peak(samplerate=1,distance=distance,threshold=threshold)
#    temp_tag=test.moving_avg.peak_x-5
#    dev02.eu.plot_ts(tag=temp_tag,index=[2])   
#
#    
    