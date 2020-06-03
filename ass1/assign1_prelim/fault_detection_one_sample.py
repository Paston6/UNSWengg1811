#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for fault_prediction_one_sample

@author: XING XING z5142063
"""
import power_prediction as pred
# Compare predicted power generated vs measured power to determine fault
# [][][][][][][][][][][][][[][][][][][][][][][][][] 100%

def fault_detection_one_sample(irradiance_average_one_sample, power_one_sample,model_para,margin):
    # Get the predicted_power by calling the power_predict
    predicted_power = pred.power_prediction(irradiance_average_one_sample, model_para)
    
    # Get the absolute difference
    difference = predicted_power - power_one_sample
    
    # Distinguish the Boolean Value
    if(difference >= -margin and difference <= margin):
        return False
    else:
        return True
