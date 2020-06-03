#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

You can use this file to test your classify_a_pixel().

This file containing 7 test cases which you can choose by
adjusting the variable test_num in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import classify_a_pixel as classify_1 # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_num = 0 # test_num can be 0, 1, 2, 3, 4, 5, 6

# The tests are based on using different pixels from this Boolean array: 
concrete_crack_bool = np.array(
      [[ True,  True, False, False, False],
       [ True,  True,  True, False, False],
       [False,  True,  True,  True, False],
       [False, False,  True, False, False],
       [False, False,  True, False, False],
       [False,  True,  True,  True, False]])

if test_num == 0:  
    # A corner pixel with expected answer 2
    i = 0
    j = 0 
    expected_answer = 2
elif test_num == 1:     
    # A corner pixel with expected answer 0
    i = 5
    j = 4 
    expected_answer = 0
elif test_num == 2:     
    # An edge pixel with expected answer 2
    i = 5
    j = 2 
    expected_answer = 2
elif test_num == 3:     
    # An edge pixel with expected answer 1
    i = 5
    j = 1 
    expected_answer = 1    
elif test_num == 4:     
    # An inner pixel with expected answer 2
    i = 1
    j = 1 
    expected_answer = 2
elif test_num == 5:     
    # An inner pixel with expected answer 1
    i = 3
    j = 2 
    expected_answer = 1 
elif test_num == 6:     
    # A pixel with expected answer 0
    i = 3
    j = 3 
    expected_answer = 0        
else:
    print('Not a valid test number')    
    
# %% # %% Run the function and check the answers

# Call the function () and store the answer in your_answer
your_answer = classify_1.classify_a_pixel(concrete_crack_bool,i,j)

# Do some basic checks before making a comparison 
# These basic checks are: Is it an int? Is it 0,1,2
#                        
# If all these types are correct, then compare the entries 
if type(your_answer) is int:
    if your_answer in [0,1,2]:
        if your_answer == expected_answer:
            print('Your answer is correct')
        else:
            print('Your answer is NOT correct')
    else:
        print('Your answer is not 0, 1 or 2')
else:
    print('Your answer is not an integer')      
    
# Plot the image
print('')
print('The given Boolean image')
print('The red dot marks the pixel used in the test')

fig, ax = plt.subplots()
plt.imshow(concrete_crack_bool, cmap = 'gray', vmin = 0, vmax = 1)  # Plot the image 
plt.plot(j,i,'ro',markersize = 8)  # Mark the pixel used in the test 
# The next 6 lines of code are needed to place the grid 
# exactly at the pixel boundaries 
ax.set_xticks(np.arange(0,concrete_crack_bool.shape[1]), minor=False)
ax.set_xticks(np.arange(0.5,concrete_crack_bool.shape[1]), minor=True)
ax.xaxis.grid(which='minor', color='blue')
ax.set_yticks(np.arange(0,concrete_crack_bool.shape[0]), minor=False)
ax.set_yticks(np.arange(0.5,concrete_crack_bool.shape[0]), minor=True)
ax.yaxis.grid(which='minor', color='blue')
plt.title('The given Boolean image')

   