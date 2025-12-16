#BROADCASTING:
# NumPy automatically repeats or stretches a smaller array so it can match a bigger one during math operations — no loop needed.
'''
👉 Broadcasting means NumPy automatically stretches the single value discount so it can be used with the entire prices array in element-wise calculations.
'''
import numpy as np
prices = np.array([100,200,300])
discount = 10 #scalar single value

# NumPy broadcasts the scalar: 10 → [10, 10, 10] so it can work with: prices = [100, 200, 300]
final_prices = prices-(prices*discount/100)
print(final_prices)# [ 90. 180. 270.]

# --------------------------------------------------------------------------
#HOW NumPy HANDLES ARRAYS OF DIFFERENT SHAPE(ROWS AND COLUMNS):
"""
📐 Broadcasting Rules:Two dimensions are compatible if:
They are equal, or
One of them is 1

NumPy compares dimensions from RIGHT to LEFT.

1) Matching dimensions:

2) expanding single elements/Scalar Broadcasting(Adding scalar to array)
3) incompatible shapes:
"""
# --------------------------------------------------------------------------

# 1) Matching dimensions:
matrix=np.array([[1,2,3],[4,5,6]])# shape (2x3) ,matrix
vector=np.array([10,20,30])# shape (3,) ,1d array
# NumPy treats vector as shape (1,3) and broadcasts it to (2,3).
result=matrix +vector 
print(result) # [[11 22 33]
                # [14 25 36]]

# --------------------------------------------------------------------------

#2) expanding single elements/Scalar Broadcasting(Adding scalar to array)
arr=np.array([100,200,300])
result = arr*2 #Scalar 2 becomes [2,2,2].
print(result) #[200 400 600]

# --------------------------------------------------------------------------

#3) incompatible shapes:
arr1 = np.array([[1,2,3],[4,5,6]])#shape(2,3)
arr2 = np.array([1,2])#shape(2,)
"""result = arr1 + arr2
print(result)

Right-to-left comparison:
(3 vs 2) → Not equal AND neither is 1 → ❌ Incompatible
"""
# This will raise an error:
# ValueError: operands could not be broadcast together
# result = arr1 + arr2

# -------------------------------------------------------------------------
# SOLUTION TO THIS ERROR → Use reshape() to make dimensions compatible
"""
Goal:
We want arr2 to match shape (1,3) or (2,3).
Your array (2,) does not have a trailing 1.
It is like (2) → its last dimension is 2, not 1.
"""

# Example solution: reshape arr2 to (2,1) → can broadcast to (2,3)
arr2_fixed = arr2.reshape(2,1)   # shape becomes (2,1)
result_fixed = arr1 + arr2_fixed
print(result_fixed) # [[2 3 4]
#                      [6 7 8]]
# arr2_fixed broadcasts to:
# [[1 1 1]
#  [2 2 2]]



#---------------------------------------------------------------------------------------------------------------------------------------
#VECTORIZATION:performing operation on ann entire array at one time without using loops
#used in matrix operation

#Python list loop (slow for large data)
list1 = [1,2,3]
list2 = [4,5,6]
result =[x+y for x,y in zip(list1,list2)]#list comprehension
print(result)# [5, 7, 9]
'''list comprehension will only work for small list but if you work with  big list this will slow down thats why vectorization is needed'''
# vectorization addition-------------------------------------------------------------------------------------------------------------------
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=arr1+arr2# vectorization addition

print (result)#[5 7 9]
#vectorization multiplication-------------------------------------------------------------------------------------------------------------------

arr=np.array([10,20,30])

multiplied = arr*3

print (multiplied)# [30 60 90]

#dot productss-------------------------------------------------------------------------------------------------------------------
print("dot products:",np.dot(arr1,arr2))

#angles between two vectors:-----------------------------------------------------------------------------------------------------------------
angle=np.arccos(np.dot(arr1,arr2)/(np.linalg.norm(arr1)*np.linalg.norm(arr2))) 
print("angle of vectors:",angle)# ✔ Output is in radians

#vectorize(matrix) operation: operation performs on every elements of matrix---------------------------------------------------------------------------------------
restaurant_types = np.array(['biryani','chinese','pizza','burger','cafe'])
vectorized_upperCase=np.vectorize(str.upper)
'''
🔴 Important clarification:
np.vectorize() is NOT true vectorization
It is just a loop under the hood
Useful for convenience, not performance
✔ Best for string operations and readability'''

print("Vectorized Upper",vectorized_upperCase(restaurant_types))


