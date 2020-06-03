#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your power_prediction().

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import power_prediction as pred

# %% Tests 
test_num = 3

if test_num == 0:
    irradiance_average_one_sample = 251.54
    model_para = [0.086, 3.44e-5, 3e-3]  
    expected_answer = 27.980249
elif test_num == 1: 
    irradiance_average_one_sample = 671.34
    model_para = [0.086, 3.44e-5, 3e-3]  
    expected_answer = 86.349041
elif test_num == 2: 
    irradiance_average_one_sample = 427.34
    model_para = [0.091, 1.44e-5, 5.2e-3]  
    expected_answer = 54.978621
elif test_num == 3: 
    irradiance_average_one_sample = 813.68
    model_para = [0.075, 7.14e-5, 2.3e-3]  
    expected_answer = 120.839907


# %% Run the function and check the answers
TOL = 1e-4 # Tolerance for comparing float     
    
your_answer = pred.power_prediction(irradiance_average_one_sample,model_para)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if abs(your_answer - expected_answer) <= TOL: 
    print('Your answer is within the tolerance')
else:
    print('Your answer is not within the tolerance')  
        
        
