#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 18s2 exam 

Template for Question 1a. 
"""

def q1a_func(a_list,a,b):
        
    for i in a_list:
        if(i < a or i >= b):
            return False
            
    return True
