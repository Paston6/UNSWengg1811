#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Mid-term exam

Template for m3.py 
"""

#%% Define list_a
list_a = [12.5, 1.3, -3.67]
# For list_a = [12.5, 1.3, -3.67]
# list_b is expected to be 
# [0.8518518518518519, 0.13043478260869568, 1.749063670411985]

# If you want to use other list_a to test, you can 
# modify the lines above 
#
# %% 
# You must put your code for computing list_b from list_a 
# between the lines indicatd below
#
# You can add additional lines but your code must be
# between these two lines   
#  
#-*-*-* Your code below here
list_b = []
for i in list_a:
    list_b.append((i-1)/(i+1))

#-*-*-* Your code above here 
#

# For list_a = [12.5, 1.3, -3.67]
# list_b is expected to be 
# [0.8518518518518519, 0.13043478260869568, 1.749063670411985]
# You need to manually check list_b values against expected values 
print(list_b)



