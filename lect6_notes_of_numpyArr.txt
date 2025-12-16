#HANDLING MISSING VALUES (NumPy)-----------------------------------------------------------------

#1) np.isnan(array):
'''Purpose: Detects missing values (NaN) in an array
NaN = Not a Number
Common causes:
Division by zero
Empty or undefined values
Returns: Boolean array (True where value is NaN)
@interviw_question:can we comapre them directly
print(np.nan == np.nan)
answer: NO!! we cannot compare nan values directly
'''
#CODE:
import numpy as np
arr1=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr1)) # [False False  True False  True False]


'''2)np.nan_to_num(array,nan=value)-you can replace a mising value with another number(default number is "0" )'''
#CODE:

arr1=np.array([1,2,np.nan,4,np.nan,6])
cleaned_arr = np.nan_to_num(arr1)

print(cleaned_arr)# default value is '0' : [1. 2. 0. 4. 0. 6.]
 
cleaned_arr = np.nan_to_num(arr1,nan=100)
print("replaced with 100",cleaned_arr)# replaced with 100 [  1.   2. 100.   4. 100.   6.]


'''3)np.isinf(array)-detect infinite values 
example:10*1000
divide by zero (1/0) 
Returns: Boolean array (True where value is infinite)
'''
#CODE:
arr1=np.array([1,2,np.inf,4,-np.inf,6])

print("infinituve value present in:",np.isinf(arr1))# infinituve value present in: [False False  True False  True False]

#REPLACING INFINITE VALUE WITH FINITE VALUE:-------------------------------------

arr1=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr1))
cleaned_arr1 = np.nan_to_num(arr1,posinf = 100 , neginf = -100)#if positive infinity present then replace with 100,if neg infinity present then replace with -100
print(cleaned_arr1)