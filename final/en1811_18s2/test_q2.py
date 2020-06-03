#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 18s2 exam 

Test file for Question 2
"""

import numpy as np 

# Test case 0
filename_0 = 'data_file_1.txt'
data_array_expected_0 = np.array([[1.6, 2.3, 4.5, 8.9],
                                  [2.6, 1.9, 1.7, 6.7],
                                  [1.4, 1.5, 1.6, 1.1]])
data_value_expected_0 = 3

# Test case 1 
filename_1 = 'sample.txt'
data_array_expected_1 = np.array([[8.9, 3.7],
                                  [6.7, 9.7],
                                  [1.1, 5.7],
                                  [1.4, 1.5],
                                  [2.6, 1.9],
                                  [1.9, 1.7]])
data_value_expected_1 = 51

# Test case 2 
filename_2 = 'somefile.txt'
data_array_expected_2 = np.array([[2.6, 1.9, 1.7, 6.7, 9.7]])
data_value_expected_2 = 102

file_name_all = [filename_0,filename_1,filename_2]
data_array_expected_all = [data_array_expected_0,
                           data_array_expected_1,
                           data_array_expected_2]
data_value_expected_all = [data_value_expected_0,
                           data_value_expected_1,
                           data_value_expected_2]

# %% Run the tests 
import q2
for test_case in range(3):
    data_array,data_value = q2.q2_func(file_name_all[test_case])
    
    if np.all(data_array==data_array_expected_all[test_case]):
        print('Test case',str(test_case),':',
              'The data array is correct')
    else:
        print('Test case',str(test_case),':',
              'The data array is NOT correct')    
        
    if data_value==data_value_expected_all[test_case]:
        print('Test case',str(test_case),':',
              'The data value is correct')    
    else:
        print('Test case',str(test_case),':',
              'The data value is NOT correct')  
    
