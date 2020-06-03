#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

File for calc_average

@author: XING XING z5142063
"""
# Calculate the summary through the segmentation list
# [][][][][][][][][][][][[][][][][][][][][][][] 100%

def calc_average(time_series, segment_length):
    # Global variables x3
    padding = int(len(time_series)/segment_length)
    result = []
    index = 0
    
    # Padding through time_series
    for i in range(0, padding):
        sum = 0
        # Sum the partial result through segment
        for j in range(0, segment_length):
            sum = sum + time_series[index]
            index = index + 1
        # Append partial average to the result list
        result.append(sum/segment_length)
    
    return result
