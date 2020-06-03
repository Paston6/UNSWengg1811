#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

File for fault_detection_time_series

@author: XING XING z5142063
"""
import fault_detection_one_sample as one 
# Performing fault detection for a time-series
# [][][][][][][][][][][][][[][][][][][][] 100%

def fault_detection_time_series(irradiance_time_series_average,power_time_series,model_para,margin):
    # get the size of the data set
    length = int(len(irradiance_time_series_average))
    result = []
    
    # trough all elements in the index list detect the faults
    for index in range(0, length):
        # extract the parameters from arrays
        irradiance_average_one_sample = irradiance_time_series_average[index]
        power_one_sample = power_time_series[index]
        
        # calling fault_detection_one_sample() for distinguish Ture or False
        indication = one.fault_detection_one_sample(irradiance_average_one_sample,power_one_sample,model_para,margin)
        
        # if there is a fault add it into the list
        if(indication == True):
            result.append(index)
        
    return result
