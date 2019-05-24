# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:53:31 2019

@author: 180218
"""

import datetime
t=list(datetime.datetime.strptime("2014-12-31 18:20:10.100", "%Y-%m-%d %H:%M:%S.%f").timetuple())

datetime.datetime.now().date().month
tl=list(datetime.datetime.now().date().timetuple())
#datetime.datetime.date()
#datetime.datetime.day
#print(datetime.datetime)
#datetime.datetime(2014, 12, 31, 18, 20, 10)


datetime.datetime.strptime("2014-12-31 18:20:10.999", "%Y-%m-%d %H:%M:%S.%f").microsecond
dd = datetime.datetime.strptime("2018-12-23 09:16:43.282", "%Y-%m-%d %H:%M:%S.%f")
datetime.datetime.strptime("2014-12-31 18:20:10.100", "%Y-%m-%d %H:%M:%S.%f").timetz()
