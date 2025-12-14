# Numpy for Data Science _ Full Course _ Sagar Chouksey - YouTube and chai and code too 
# ✅ 1. Creating a Python List vs NumPy Array:
'''Lists are the most common Python data structure.
✔️ Properties
Ordered (can be indexed)
Mutable (you can change elements)
Can contain mixed data types
Created using square brackets [ ]
General-purpose container
Can store mixed types (int, float, string, etc.)
Not optimized for numerical operations
Example:

my_list = [1, 2, 3, "hello", 4.5]
my_list[0] = 10  # allowed '''

python_list=[1,2,3,4,5] 
print(python_list)#[1, 2, 3, 4, 5]

'''✅ 3. ARRAYS (NumPy arrays)
These come from the NumPy library, not built into Python.
✔️ Properties
Fast, optimized for math and scientific computing
Elements must be same type (usually numbers)
Support vectorized(1D array) operations (add, multiply, reshape, etc.)
Created using np.array() with brackets
Optimized for numerical computation
Faster, uses less memory
Supports vectorized operations (e.g., array * 2)
Example : '''

'''
import numpy as np 
numpy_array=np.array([1,2,3,4,5])
print(numpy_array) #[1 2 3 4 5]'''


import numpy as np
arr = np.array([1, 2, 3])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

# You can do math with them directly:
arr * 2   # → array([2, 4, 6])

"""creating arrays from python list:Simply converts a Python list into a NumPy array.
syntax: np.array([lis_element_1,list_elemen2,l_e3])"""

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr)

"""creating arrays with  default values:filling every value with zero for now,later can be changed
syntax : np.zeros(shape)#shape-no of rows and columns
Creates an array where every value is 0
Shape can be a single number or a tuple (Tuples are like lists but immutable.
✔️ Properties
Ordered(can be indexed)
Immutable (cannot change elements)
Can contain mixed types
Created using parentheses ( ))"""

import numpy as np
zeros_arr=np.zeros(3)
print(zeros_arr) #[0. 0. 0.]

"""creating arrays with  default values:filling every value with ones for now,later can be changed
syntax : np.ones(shape)#shape is no of rows and column
shape must be a tuple for multi-dimensional arrays
Useful for initialization"""
import numpy as np
ones_arr=np.ones((2,3))#tuples format otherwise error
print(ones_arr) #[[1. 1. 1.]
                # [1. 1. 1.]]


"""creating arrays with  default values:filling every value with other number than 0 or 1 for now,later can be changed
syntax : np.full(shape,value) #shape is no of rows and column"""
import numpy as np
filled_arr=np.full((2,3),8) #shape must be tuples format otherwise error
print(filled_arr) #[[8 8 8]
                  # [8 8 8]]



"""creating sequences of numbers in numpy : arange()
syntax : np.arange(start,stop[exclusive],step)"""
import numpy as np
arr=np.arange(1,10,2) #tuples format otherwise error
print(arr) #[1 3 5 7 9]


import numpy as np
arr=np.arange(12)#non-inclusive means 12 will not include
print(arr)#[0 1 2 3 4 5 6 7 8 9 10 11]



"""creating identity matrices in numpy : it is a square matrix with ones on diagonals and zero everywhere .
What is an identity matrix?
A square matrix where:
Diagonal = 1
Other elements = 0
syntax : np.eye(size)"""
import numpy as np
identity_matrix=np.eye(3) #tuples format otherwise error
print(identity_matrix) #[[1. 0. 0.]
                        # [0. 1. 0.]
                        # [0. 0. 1.]]

import numpy as np
identity_matrix=np.eye(4) #tuples format otherwise error
print(identity_matrix)
                    #    [[1. 0. 0. 0.]
                    #     [0. 1. 0. 0.]
                    #     [0. 0. 1. 0.]
                    #     [0. 0. 0. 1.]]
					
					
"""creating arrays with random values:
use numpy random functions to fill array with random numbers
syntax : np.random.rand(shape) -> random floats (0 to 1)
         np.random.randint(low, high, shape) -> random integers
		 np.random.random(shape)
# shape must be your array dimension in tuple format
"""

import numpy as np

# random float values between 0 and 1
random_arr = np.random.rand(2, 3)  # shape must be in tuple format
print(random_arr)
# example output (changes every time):
# [[0.12 0.88 0.45]
#  [0.34 0.90 0.23]]

# random integer values between 0 and 9
random_int_arr = np.random.randint(0, 10, (2, 3))
print(random_int_arr)
# example output (changes every time):
# [[3 9 1]
#  [7 0 4]]

random_arr = np.random.random((2, 3))  # 2x3 array with random floats
print(random_arr)
# example output (different every run):
# [[0.12 0.88 0.45]
#  [0.34 0.90 0.23]]


#Vector(1D array), Matrix(2D array) and Tensor(3D array):

vector = np.array([1, 2, 3])
print("Vector: ", vector)

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print("Matrix: ", matrix)
#or
matrix = np.array([
                    [1, 2, 3], 
                    [4, 5, 6]
                   ])
print("Matrix: ", matrix)

tensor = np.array([[[1, 2], [3, 4]], 
                   [[5, 6], [7, 8]]])
print("Tensor: ", tensor)
#or
tensor = np.array([
                   [ 
                    [1, 2], [3, 4]
                    ], 
                   [
                    [5, 6], [7, 8]
                    ]
                   ])
print("Tensor: ", tensor)