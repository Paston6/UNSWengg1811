#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Midterm exam

Template file m1.py 
"""

#%% You can modify the check below 
# 
# Define x  
x = 150
# For x = 150, the output string 
# should be 'need-monitoring'
expected_answer = 'need-monitoring'

# If you want to use other x to test, you can 
# modify the lines above 
#

#
# %% 
# You must put your code for determining output_string 
# from x in between the two lines indicated below
#
# You can add additional lines but your code must be
# between the two lines indicated below 
#  
#-*-*-* Your code below here

if (x > 300):
    output_string = 'good-performance'
elif(x <= -200):
    output_string = 'alert'
else:
    output_string = 'need-monitoring'

        
#-*-*-* Your code above here 
#

# Compare your answer against expected
if output_string == expected_answer:
    print('m1, Sample Test Passed: Correct output_string')
else: 
    print('m1, Sample Test Failed: Incorrect output_string')    
    
     
