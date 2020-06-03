#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

File for power_prediction

@author: XING XING z5142063
"""
import math
# calculate expected power generated use the average irradiance and models
#[][][][][][][][][][][][][][][][[][][][][][][][][][][][][][][][][][] 100%

def power_prediction(irradiance_average_one_sample, model_para):
    # extract parameters and assign G as irradiance_average_one_sample
    var_a0 = model_para[0]
    var_a1 = model_para[1]
    var_a2 = model_para[2]
    var_G = irradiance_average_one_sample
    
    # P = G (a0 + a1 G + a2 log(G))
    var_P = var_G*(var_a0 + var_G * var_a1 + math.log(var_G) * var_a2)
    
    # Return float result
    return var_P
