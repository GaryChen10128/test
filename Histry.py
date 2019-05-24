# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:16:33 2019

@author: 180218
"""

class Histry:
#    @classmethod
    def __init__(self,date):
        self._date=date
        if self._date=='190117':
            self.body_table=['head','c4','t4','t7','rs','0','c7','ls']
            self.dev_id=self.body_table.index(dev_name)
            self.scale=[1,1,1,1]
            if raw_or_cali=='raw':
                self.str_path=[
                 ['./raw/190117CROM/20190117083545.csv','./raw/190117CROM/20190117083926.csv','./raw/190117CROM/20190117084258.csv','./aiq_data/1025/20181025091654.csv','./aiq_data/1025/20181025094026.csv',''] #1
                ,['./aiq_data/1121/20181121100728.csv','./aiq_data/1121/20181121101639.csv','./aiq_data/1121/20181121110301.csv','./aiq_data/1121/20181121114908.csv','','']] #12-2 (sample size right)
                self.bias=np.array([[0,0,0,0,0,0],
                       [0,0,0,0,0,0]])*31*60
            if raw_or_cali=='cali':
                self.str_path=['./raw/190117CROM/D02/01.csv','./raw/190117CROM/D02/01.csv','./raw/190117CROM/D02/23.csv','./raw/190117CROM/D02/23.csv','./raw/190117CROM/D02/45.csv','./raw/190117CROM/D02/45.csv','./raw/190117CROM/D02/67.csv','./raw/190117CROM/D02/67.csv']
                self.pathway=self.str_path[self.dev_id]


        
        
        