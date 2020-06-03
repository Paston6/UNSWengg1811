#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Mid-term exam

Template for m4.py 

There are three test cases in this file. You can select them using
the variable test_num in Line 14. 

"""

# %% Select the test case
test_num = 0 # 0, 1 or 2

if test_num == 0:
    list_x = [19, -2, -15, -8, -9, 14, 7, -7, 12, 9, -6,  5, 3]
    n = 3 
    expected_output = [5, 12, 14, 14]
    
elif test_num == 1:
    list_x = [12.1, 2.1, 8, -3, -2, -5.1]
    n = 2
    expected_output = [-2, 8, 12.1]

elif test_num == 2:
    list_x = [8.7, 6.7, -0.4, -1.7]
    n = 1
    expected_output = [-1.7, -0.4, 6.7, 8.7] 
    
else:
    print('test_num can only be 0, 1 or 2')

# If you want to use other list_x or n to test, you can 
# modify the lines above 
#
# %% 
# You must put your code for computing list_max from list_x and n  
# between the lines indicatd below
#
# You can add additional lines but your code must be
# between these two lines   
#  
#-*-*-* Your code below here
import math
list_max = []
i = 1

while((i * n) <= len(list_x)):
    max = -math.inf
    for num in list_x[-i*n:]:
        if (num > max):
            max = num
    list_max.append(max)
    i = i + 1


#-*-*-* Your code above here 
# 
# %%
# Compare your answer against expected answer
print('Your output is', list_max)
print('The expected outputm is', expected_output)
    
