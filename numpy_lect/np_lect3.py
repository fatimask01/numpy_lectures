#1️⃣ INDEXING(1D & 2D)
# INDEXING: Basic Indexing (arr[0]): Returns a scalar value eg 10
'''array[index] #1d array
array[row,column] #2d array'''

# 1D Indexing
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])#10
print(arr[2])#30
print(arr[-1])#50

# 2D Indexing

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Specific element:", arr_2d[0, 2])   # 3
print("Entire row:", arr_2d[1])            # [4 5 6]
print("Entire column:", arr_2d[:, 1])      # [2 5 8]


#2️⃣ SLICING
'''array[start : stop(exclusive) : step]


negative step will access in revers order (-1)'''

arr=np.array([10,20,30,40,50,60])
print(arr[1:5]) #[20 30 40 50] 
print(arr[:4]) #[10 20 30 40] 
print(arr[::2]) #[10 30 50]  
print(arr[::-1]) #[60 50 40 30 20 10] negaative indexin will revere an array




arr_2d = np.array(
    [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]   
    ]
)

print("specific element:", arr_2d[0, 2])   # element in row 0, column 2 → 3
print("entire row:", arr_2d[1])           # second row → [4 5 6]
print("entire column:", arr_2d[:, 1])     # second column → [2 5 8]


#3️⃣FENCY INDEXING(Selecting multiple elements at once using lists/arrays.) vs where

'''Fancy Indexing (arr[[0,2,4]])
Always returns a NumPy array
 Even if you pick a single element'''

arr=np.array([10,20,30,40,50,60])
print(arr[[0,2,4]]) #[10 30 50] copy

#or
indices=[0,2,4]
print(arr[indices]) # [10 30 50] # NumPy array

#np.where():Returns indices where condition is true.
'''np.where()
Returns a tuple of NumPy arrays
Inside the tuple → NumPy array(s) of indice
Each array contains indices where the condition is True
'''
arr = np.array([10, 20, 30, 40, 50, 60])

where_result = np.where(arr > 25)
print("Indices:", where_result) #(array([2, 3, 4, 5]),) Returns a tuple of NumPy arrays
print("Values:", arr[where_result])    # [30 40 50 60]


#CONDITION ARRAY(Ternary-like Operation)
numbers=np.array([1,2,3,4,5,6,7,8,9,10])
condition_array = np.where(numbers > 5,"true","fale")
print(condition_array) #['fale' 'fale' 'fale' 'fale' 'fale' 'true' 'true' 'true' 'true' 'true']

#BOOLEAN MASKING/FILTERING DATA BASED ON CONDITIONS:(10x faster then loop for filtering)

arr=np.array([10,20,30,40,50,60])
print(arr[arr>25]) #[30 40 50 60]

#OR
numbers=np.array([1,2,3,4,5,6,7,8,9,10])
mask=numbers>5
print("numbers greater than 5",numbers[mask]) #[ 6  7  8  9 10]

#   SORTING IN ARRAY:
# Sort 1D array
unsorted=np.array([3,1,4,1,5,9,2,6])
print("Sorted array:",np.sort(unsorted))  #[1 1 2 3 4 5 6 9]

arr_2d_unsorted =np.array([[3,1],[1,2],[2,3]])
print("Sorted 2D array by coloumn",np.sort(arr_2d_unsorted,axis=0)) # [[1 1]
                                                                    #  [2 2]
                                                                    #  [3 3]]
print("Sorted 2D array by row",np.sort(arr_2d_unsorted,axis=1)) #[[1 3]
                                                                # [1 2]
                                                                # [2 3]]