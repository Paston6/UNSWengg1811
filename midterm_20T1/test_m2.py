#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Mid-term exam

Test file for m2.py 
"""

# This file tests the function m2_func
# in the file m2.py
#
# This file and m2.py must be in the same directory
# 
# This file contains only one test case 
# 

# Import the file m2 
import m2 

# Call the function with 
#   The first input = 5 
#   The second input = 3
in1 = 1
in2 = 5
#   The expected answers are
out1_expected = -0.653644
out2_expected = 0.057143 

TOL = 1e-5   # Tolerance for comparison

# Let's call your function
out1, out2 = m2.m2_func(in1,in2)


# Compare your answers against expected answers
if abs(out1-out1_expected)< TOL and abs(out2-out2_expected) < TOL:
    print('m2, Sample Test Passed: The outputs are within the tolerance')
else: 
    print('m2, Sample Test Failed: The outputs are NOT within the tolerance')    

# =============================================================================
# # An additional test 
## Call the function with 
##   The first input = 1 
##   The second input = 5
#in1 = 1
#in2 = 5
##   The expected answers are
#out1_expected = -0.653644
#out2_expected = 0.057143   
# =============================================================================
