#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

File for find_false_alarms

@author: XING XING z5142063
"""
# Determining the false alarms
# [][][][][][][][][][][][] 100%

def find_false_alarms(your_fault_list,true_fault_list):
    result = []
    
    # for each elements in ypur_fault_list check if its in true_
    for i in your_fault_list:
        if(i in true_fault_list):
            pass
        else:
            # if its not in append to the result
            result.append(i)
    
    return result


