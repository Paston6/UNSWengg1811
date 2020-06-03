#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your calc_average().

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import calc_average as calc 

# %% Tests 
test_num = 3

if test_num == 0:
    time_series = [100,200,300,400]
    segment_length = 4 
    expected_answer = [250]
elif test_num == 1: 
    time_series = [100,200,300,400,500,600] 
    segment_length = 3
    expected_answer = [200,500]
elif test_num == 2: 
    time_series = [240.2, 220.1, 260.2, 280.7, 256.5,
                   320.3, 300.7, 267.1, 321.2, 234.5, 
                   421.7, 476.2, 321.6, 329.7, 323.4,
                   407.9, 456.7, 489.3, 521.5, 534.6] 
    segment_length = 5
    expected_answer = [251.54, 288.76, 374.52, 482.00]
elif test_num == 3: 
    time_series = [240.2, 220.1, 260.2, 
                   280.7, 256.5, 320.3, 
                   300.7, 267.1, 321.2, 
                   234.5, 421.7, 476.2, 
                   321.6, 329.7, 323.4,
                   407.9, 456.7, 489.3]  
    segment_length = 3
    expected_answer = [240.16666, 285.83333, 296.33333, 377.46667, 324.9, 451.30]


# %% Run the function and check the answers
TOL = 1e-4 # Tolerance for comparing float     
    
your_answer = calc.calc_average(time_series,segment_length)
print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if len(your_answer) != len(expected_answer):
    print('We are expecting',len(expected_answer),'entries')
    print('but your answer has ',len(your_answer),'entries')
else:
    within_tolerance = [True if abs(y - e) <= TOL else False for 
                        y, e in zip(your_answer,expected_answer)]
    if all(within_tolerance):
        print('Your answer is correct')
    else:
        print('Some values in your list are not correct!')    
