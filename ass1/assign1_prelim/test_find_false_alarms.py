#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your find_false_alarms().

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_false_alarms as ffa

# %% Tests 
test_num = 2

if test_num == 0:
    your_fault_list = [1, 10]
    true_fault_list = [1]
    expected_answer = [10]
elif test_num == 1: 
    your_fault_list = [3, 5, 7, 123]
    true_fault_list = [7]
    expected_answer = [3, 5, 123]
elif test_num == 2: 
    your_fault_list = [13, 17, 19, 31]
    true_fault_list = [13, 14, 17, 18, 19, 31, 33]
    expected_answer = []

# %% Run the function and check the answers     
    
your_answer = ffa.find_false_alarms(your_fault_list,true_fault_list)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

comparison_output = your_answer == expected_answer
if comparison_output:
    print('Your answer is correct')
else:
    print('Some values are not correct')        
        
