# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:44:45 2018

@author: Fanhsiao
"""

time = Now[Now.columns[0]]
time_formated = pd.DataFrame(pd.to_datetime(time, format = '%Y-%m-%dT%H:%M:%SZ'))
time_formated['year'] = pd.DatetimeIndex(time_formated['sample_dt']).year
time_formated['month'] = pd.DatetimeIndex(time_formated['sample_dt']).year
time_formated['hour'] = pd.DatetimeIndex(time_formated['sample_dt']).year
time_formated['minute'] = pd.DatetimeIndex(time_formated['sample_dt']).year
time_formated['second'] = pd.DatetimeIndex(time_formated['sample_dt']).year