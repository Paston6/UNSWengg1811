#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 18s2 exam 

Template for Question 1b. 
"""

def q1b_func(a_list,m):
   
        
    index = 0
    ind = 0
    res = []
    for l in a_list:
        if(true(l,m) == True):
            res.append(index)
        index = index + 1
    return res
            


def true(l,m):
    for x in l:
        if(x > m):
            return False
    return True
