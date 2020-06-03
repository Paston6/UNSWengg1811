#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your fault_detection_one_sample().

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import fault_detection_one_sample as one

# %% Tests 
test_num = 3

if test_num == 0:
    irradiance_average_one_sample = 251.54
    power = 31.2
    model_para = [0.086, 3.44e-5, 3e-3] 
    margin = 10 
    expected_answer = False
elif test_num == 1: 
    irradiance_average_one_sample = 876.32
    power = 56.7
    model_para = [0.086, 3.44e-5, 3e-3] 
    margin = 10 
    expected_answer = True
elif test_num == 2: 
    irradiance_average_one_sample = 288.76
    power = 20.5
    model_para = [0.089, 1.44e-5, 3e-3] 
    margin = 5.3 
    expected_answer = True
elif test_num == 3: 
    irradiance_average_one_sample = 551.54
    power = 65.6
    model_para = [0.079, 2.44e-5, 4e-3] 
    margin = 2.3 
    expected_answer = False


# %% Run the function and check the answers     
    
your_answer = one.fault_detection_one_sample(irradiance_average_one_sample,power,model_para,margin)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if your_answer == expected_answer:
    print('Your answer is correct')
else:
    print('Some values are not correct')        
        
