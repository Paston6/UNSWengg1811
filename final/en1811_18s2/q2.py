#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 18s2 exam 

Template file for Question 2 
"""

import numpy as np 

def q2_func(filename):
    with open(filename,'r') as file:
        contents = file.readlines()
        array_num_rows = len(contents)-1
        array_num_cols = len(contents[0].split())

        data_array = np.zeros((array_num_rows,array_num_cols),dtype=float)

        for i in range(array_num_rows):
            row_str = contents[i].split()
            for j in range(array_num_cols):
                data_array[i,j] = float(row_str[j])

        data_value = int(contents[-1])

    return data_array, data_value 
    
    
