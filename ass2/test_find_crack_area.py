#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

You can use this file to test your find_crack_area().

This file containing 5 test cases which you can choose by
adjusting the variable test_num in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_crack_area as area # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_num = 0 # test_num can be 0, 1, 2, 3, 4

# The thresholds for the tests 
expected_answer_list = [13,25,10,30,94]

if test_num == 0:
    # Boolean array after thresholding      
    concrete_crack_bool = np.array(
      [[ True,  True, False, False, False],
       [ True,  True,  True, False, False],
       [False,  True,  True,  True, False],
       [False, False,  True, False, False],
       [False, False,  True, False, False],
       [False,  True,  True,  True, False]])
    
    # The expected answer  
    expected_answer = expected_answer_list[test_num]
    
elif 1 <= test_num <= 4: 
    # Load the concrete image and expected answer from the ref file 
    ref_data = np.load('ref_data_' + str(test_num) + '.npz', allow_pickle = True)
    concrete_crack_bool = ref_data['concrete_crack_bool']
    
    # The expected answer  
    expected_answer = expected_answer_list[test_num]
     
else: 
    print('Not a valid test number')


# %% Run the function and check the answers

# Call the function find_crack_area() and store the answer in your_answer
your_answer = area.find_crack_area(concrete_crack_bool)

if your_answer == expected_answer:
    print('Your answer is correct')
else:
    print('Your answer is NOT correct')
    print('The expected answer is', expected_answer)
    print('Your answer is',your_answer)

print('')

# Plot the given Boolean image 
plt.figure()
fig, ax = plt.subplots()
plt.imshow(concrete_crack_bool, cmap = 'gray', vmin = 0, vmax = 1)
# The next 6 lines of code are needed to place the grid 
# exactly at the pixel boundaries 
ax.set_xticks(np.arange(0,concrete_crack_bool.shape[1]), minor=False)
ax.set_xticks(np.arange(0.5,concrete_crack_bool.shape[1]), minor=True)
ax.xaxis.grid(which='minor', color='blue')
ax.set_yticks(np.arange(0,concrete_crack_bool.shape[0]), minor=False)
ax.set_yticks(np.arange(0.5,concrete_crack_bool.shape[0]), minor=True)
ax.yaxis.grid(which='minor', color='blue')
plt.title('The given Boolean image: White: True. Black: False')
    
