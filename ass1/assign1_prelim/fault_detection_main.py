#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for fault_detection_main

@author:  
"""
import calc_average as avg
import fault_detection_time_series as series


def fault_detection_main(irradiance_time_series,power_time_series,irradiance_sampling_time,power_sampling_time,model_para,margin):
    #===================
    # Validality check
    #===================
    # check validility of irradiance_sampling_time
    if(isinstance(irradiance_sampling_time,int) == False and irradiance_sampling_time < 0):
        return 'Corrupted input'
    
    # check validility of power_sampling_time
    if(isinstance(power_sampling_time,int) == False and power_sampling_time < 0):
        return 'Corrupted input'

    # check if irradiance_sampling_time is an integral multiple of power_sampling_time.
    if(power_sampling_time % irradiance_sampling_time != 0):
        return 'Corrupted input'
    
    # check if size of model_para is 3
    if(len(model_para) != 3):
        return 'Corrupted input'
    
    # check if margin is positive
    if(margin < 0):
        return 'Corrupted input'

    #======================================
    # Checking whether there are enough data
    #======================================
    power_times_size = len(power_time_series)
    irradiance_time_size = len(irradiance_time_series)
    if(power_times_size < 1 or irradiance_time_size < 4):
        return 'Not enough data'


    #======================================
    # Dealing with different amount of data
    #======================================
    ratio = int(power_sampling_time/irradiance_sampling_time)
    power_sampling_period = int(power_sampling_time * power_times_size)
    irradiance_sampling_period = int(irradiance_sampling_time * irradiance_time_size)
    
    # resize the irradiance_time_size and power_times_size
    if(irradiance_time_size == power_times_size * ratio):
        pass
    elif (irradiance_time_size > power_times_size * ratio):
        irradiance_time_size = power_times_size * ratio
        irradiance_time_series = irradiance_time_series[0:int(irradiance_time_size)]
    elif (irradiance_time_size < power_times_size * ratio):
        power_times_size = irradiance_time_size // ratio
        irradiance_time_size = power_times_size * ratio
        irradiance_time_series = irradiance_time_series[0:int(irradiance_time_size)]
        power_time_series = power_time_series[0:int(power_times_size)]
    
    # calling the calc_average file
    average = avg.calc_average(irradiance_time_series, int(ratio))
    
    # detect the error 
    result = series.fault_detection_time_series(average,power_time_series,model_para,margin)

    return result
