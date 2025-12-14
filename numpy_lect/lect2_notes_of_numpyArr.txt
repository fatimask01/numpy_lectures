""# ✅ NumPy Array Properties / Attributes & Operations:
''' properties/attributes of array :
                       1.shape-number of rows & columns
                       2.size-number of elements in the array
                       3.ndim(number of dimensions) 
                       4.dtype(data type of elements)
                       5.astype(convert array from one datatype to another)'''
# 1) .shape(number of column and rows):
import numpy as np
arr_2d=np.array([ #The outer pair of brackets defines the whole list that becomes the NumPy array.
                [1,2,3],
                [4,5,6]
                ])
print(arr_2d.shape) # (2,3), 2 is row and 3 is column

# 2) .size(no of elements in array):
import numpy as np
arr=np.array([  
                [10,20,30],
                [40,50,60]
                ])
print(arr.size) #6

# 3) .ndim(number of dimensions):
import numpy as np
arr_1d=np.array([1,2,3])
print(arr_1d.ndim) #1(1D array)

arr_2d=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr_2d.ndim)#2(2D array)2r,3c
       

arr_3d = np.array([
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
]) 
print(arr_3d.ndim) #3(3D array)4r,2c
print(arr_3d.shape)  # Output: (1, 4, 2)
print(arr_3d.size)  # Output: 8

'''Explanation of shape (1, 4, 2):
1️⃣ Outermost brackets → 1st dimension(number of blocks)
This contains 1 big element → so dimension 0 has size 1.
Shape so far: (1, …)

2️⃣ Second layer of brackets → 2nd dimension(rows in each block)
This contains 4 elements → so dimension 1 has size 4.
Shape so far: (1, 4, …)
               
3️⃣ Innermost brackets → 3rd dimension(columns in each row)
Each one has 2 elements → so dimension 2 has size 2.
Final shape: (1, 4, 2)'''


# 4).dtype(data type of elements in array):
import numpy as np
arr=np.array([10,20,30.5,40])
print(arr.dtype) #float64

# 5).astype(change one datatype to other data type in array):.astype() creates a new array with the converted type, while the original remains unchanged.
import numpy as np
arr =np.array([1.2,2.5,3.8])
print(arr.dtype)#float64
int_arr=arr.astype(int)
print(int_arr)#[1 2 3]
print(int_arr.dtype)#int64


#Array Reshaping:reshaping does not create a copy,it returns a view so changing values in new shape will affect array
# SYNTAX=.reshape(rows,columns)      


arr = np.arange(12)
print("Original array ", arr) #Original array  [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshaped = arr.reshape((3, 4))
print("\n Reshaped array ", reshaped) #Reshaped array  [[ 0  1  2  3]
                                                       #[ 4  5  6  7]
                                                       #[ 8  9 10 11]]


#flattening array: convert multi dimensional array into 1D array
flattened = reshaped.flatten()#no modification in original array,reyurns copy
print("\n Flattened array ", flattened) #Flattened array(copy of original array) [ 0  1  2  3  4  5  6  7  8  9 10 11]

# ravel (returns view(original) meanss modification in original array, instead of copy(flattened))
raveled = reshaped.ravel()
print("\n raveled array ", raveled) # raveled array  [ 0  1  2  3  4  5  6  7  8  9 10 11]


# Transpose(swap rows ↔ columns)
transpose = reshaped.T
print("\n Transposed array ", transpose)#Transposed array  [[ 0  4  8]
                                                            #[ 1  5  9]
                                                            #[ 2  6 10]
                                                            #[ 3  7 11]]


#OPERATIONS ON NUMPY ARRAY(Vectorized[1D array]-no need of loops):
import numpy as np
arr=np.array([10,20,30])
print(arr + 5) #[15 25 35]
print(arr * 2) #[20 40 60]
print(arr ** 2) #[100 400 900]


#AGGREGATION FUNCTIONS(SUMMARISE):
"""Aggregate functions in numpy:
used to perform operations on entire arrays like sum, min, max, mean, etc.

Common aggregate functions:
np.sum(arr)      -> total of all elements
np.min(arr)      -> smallest value
np.max(arr)      -> largest value
np.mean(arr)     -> average value (mean = sum of all values / number of values)
np.var(arr)      -> variance (Measures how far numbers are from the mean\
                              Formula: average of squared differences)
np.std(arr)      -> standard deviation (how spread out the values are\
                                        Square root of variance)

Low std/var  = values are close together
High std/var = values are spread out

🔢 Small Example

Numbers: [10, 20, 30, 40, 50]
Mean = 30

Differences from mean:

[-20, -10, 0, 10, 20]


Square them:

[400, 100, 0, 100, 400]


Variance = average = 200
Std = sqrt(200) = 14.14
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("sum:", np.sum(arr))      # 150
print("min:", np.min(arr))      # 10
print("max:", np.max(arr))      # 50
print("mean:", np.mean(arr))    # 30.0 
print("var:", np.var(arr))      # 200.0
print("std:", np.std(arr))      # 14.14...



# ⭐ Aggregate functions on 2D arrays:
two_d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(np.sum(two_d, axis=0))  # column-wise sum → [5 7 9]
print(np.sum(two_d, axis=1))  # row-wise sum → [ 6 15]

'''axis=0 (columns):
[1 2 3]
[4 5 6]
↓ ↓ ↓
5 7 9
         “Zero goes down, One goes across.”
axis=1 (rows):
[1 2 3] → 6
[4 5 6] → 15
'''