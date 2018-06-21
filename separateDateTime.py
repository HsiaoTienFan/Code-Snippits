# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:44:45 2018

@author: Fanhsiao
"""

time = Now[Now.columns[0]]
time_formated = pd.DataFrame(pd.to_datetime(time, format = '%Y-%m-%dT%H:%M:%SZ'))
Now['year'] = pd.DatetimeIndex(time_formated['sample_dt']).year
Now['month'] = pd.DatetimeIndex(time_formated['sample_dt']).month
Now['hour'] = pd.DatetimeIndex(time_formated['sample_dt']).hour
Now['minute'] = pd.DatetimeIndex(time_formated['sample_dt']).minute
Now['second'] = pd.DatetimeIndex(time_formated['sample_dt']).second
Now.assign(Mozz1_On = Now[labelNames['Curd Mill Output'][0]] >= 60)
