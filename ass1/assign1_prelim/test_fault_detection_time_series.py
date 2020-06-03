#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your fault_detection_time_series().

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import fault_detection_time_series as series

# %% Tests 
test_num = 3

if test_num == 0:
    irradiance_time_series_average = [251.54, 288.76, 374.52, 482.00]
    power_time_series = [31.2, 27.5, 55.5, 44.2]
    model_para = [0.086, 3.44e-5, 3e-3] 
    margin = 10 
    expected_answer = [2, 3]
elif test_num == 1: 
    irradiance_time_series_average = [374.52, 482.00, 876.32, 288.76, 251.54]
    power_time_series = [30.1, 54.2, 56.7, 27.5, 15.2]
    model_para = [0.086, 3.44e-5, 3e-3] 
    margin = 10 
    expected_answer = [0, 2, 4]
elif test_num == 2: 
    irradiance_time_series_average = [374.52, 482.00, 876.32, 251.54, 288.76,]
    power_time_series = [45.6, 54.2, 106.7, 35.2, 27.5]
    model_para = [0.089, 1.44e-5, 3e-3] 
    margin = 5.3 
    expected_answer = [3]
elif test_num == 3: 
    irradiance_time_series_average = [771.32, 551.54, 688.76]
    power_time_series = [93.7, 65.6, 82.7]
    model_para = [0.079, 2.44e-5, 4e-3] 
    margin = 2.3 
    expected_answer = []


# %% Run the function and check the answers     
    
your_answer = series.fault_detection_time_series(irradiance_time_series_average,
                            power_time_series, model_para, margin)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if len(your_answer) != len(expected_answer):
    print('We are expecting',len(expected_answer),'entries')
    print('but your answer has ',len(your_answer),'entries')
else:
    comparison_output = [True if y == e else False for 
                        y, e in zip(your_answer,expected_answer)]
    if all(comparison_output):
        print('Your answer is correct')
    else:
        print('Some values are not correct')        
        
