#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

You can use this file to test your test_find_threshold().

This file containing 5 test cases which you can choose by
adjusting the variable test_num in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_threshold as thres # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_num = 0 # test_num can be 0, 1, 2, 3, 4

# The thresholds for the tests 

expected_answer_list = [120.5,205.777,174.0,188.448,157.947]
num_points_list = [5,10,20,30]

if test_num == 0:
    # The concrete image     
    concrete_image = np.array(
      [[ 70, 106, 200, 216, 226],
       [ 33,  25,  38, 160, 225],
       [196,  99,  34,  29, 189],
       [218, 222,  22, 224, 221],
       [211, 192,  27, 186, 168],
       [191,  15,  28,  20, 199]])
    num_points = num_points_list[test_num]
    
    # The expected answer  
    expected_answer = expected_answer_list[test_num]
    
elif 1 <= test_num <= 4: 
    # Load the concrete image and expected answer from the ref file 
    ref_data = np.load('ref_data_' + str(test_num) + '.npz', allow_pickle = True)
    concrete_image = ref_data['concrete_image']
    
    if test_num <= 3: 
        num_points = num_points_list[test_num]
    
    # The expected answer  
    expected_answer = expected_answer_list[test_num]
         
else: 
    print('Not a valid test number')


# %% Run the function and check the answers
# Call the function find_crack_area() and store the answer in your_answer
        
if test_num <= 3:
    your_answer = thres.find_threshold(concrete_image,num_points) 
    could_run = True
elif test_num == 4:
    try:
        your_answer = thres.find_threshold(concrete_image) 
        could_run = True
    except:
        print('There is an error executing this test case.')
        print('It looks like you might not have implemented default argument')

if could_run: # If the class could be run  
    # Tolerance for testing 
    TOL = 1e-1    
    
    # Compare your_answer against the expected_answer
    if abs(your_answer - expected_answer) < TOL:
        print('Your answer is correct')
    else:
        print('Your answer is NOT correct')
        print('The expected answer is', expected_answer)
        print('Your answer is',your_answer)
    
    plt.figure()
    fig, ax = plt.subplots()
    plt.imshow(concrete_image, cmap = 'gray', vmin = 0, vmax = 255)
    # The next 6 lines of code are needed to place the grid 
    # exactly at the pixel boundaries 
    ax.set_xticks(np.arange(0,concrete_image.shape[1]), minor=False)
    ax.set_xticks(np.arange(0.5,concrete_image.shape[1]), minor=True)
    ax.xaxis.grid(which='minor', color='blue')
    ax.set_yticks(np.arange(0,concrete_image.shape[0]), minor=False)
    ax.set_yticks(np.arange(0.5,concrete_image.shape[0]), minor=True)
    ax.yaxis.grid(which='minor', color='blue')
    plt.title('The given concrete image')
        
