#NumPyARRAY MODIFICATION:
'''np.insert(array, index, value, axis=None)
array = original array
index = position number where you want to insert
value = the data to insert
axis (optional):
None → insertion into flattened array
0 → row-wise (for 2D)
1 → column-wise (for 2D)

'''
#1D array insertion: 
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)#[ 10  20 100  30  40  50  60]

#2D array insertion:axis here in mandatory
import numpy as np
arr_2d=np.array([[1,2],[3,4]])
print(arr_2d) #[[1 2]
               #[3 4]]
#insert a new row (axis=0) at index 1:
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=0)
print(new_arr_2d) #[[1 2]
                   #[5 6]
                   #[3 4]]
#insert a new column (axis=1) at index 1:

new_arr_2d=np.insert(arr_2d,1,[5,6],axis=1)
print(new_arr_2d) # [[1 5 2]
                   # [3 6 4]]
#▶ Insert into flattened array (axis=None)
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=None)
print(new_arr_2d) # [1 5 6 2 3 4]flattened array

#append:Add Elements at the End
import numpy as np
arr = np.array([10,20,30])
new_arr = np.append(arr,[40,50,60])
print(new_arr)

#concatination of array:Join Arrays
""" SYNTAX:np.concatenate((arry1,arry2),axis = 0)"""
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)

#np.delete(array,index,axix = None) : removing elements from array  #flalttened array since axis is none
#returns a new array everytime

# ⭐ 1D Delete (axis=None → flattened)
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)#[10 20 30 40 50 60]
new_arr = np.delete(arr ,0)
print(new_arr)#[20 30 40 50 60]

#2D array deletion:axis here in mandatory
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d) #[[1 2 3]
               #[4 5 6]]
#▶ Delete a row (axis=0) at index 0:
new_arr_2d=np.delete(arr_2d,0,axis=0)
print(new_arr_2d) #[[4 5 6]]

#▶ Delete a column (axis=1) at index 0:
new_arr_2d=np.delete(arr_2d,0,axis=1)
print(new_arr_2d) # [[2 3]
                   # [5 6]]

# ▶ Delete from flattened array
new_arr_2d=np.delete(arr_2d,0,axis=None)
print(new_arr_2d) # [2 3 4 5 6]flattened array

#STACKING :Combining multiple arrays together (use for merging data sset row-wise or column-wise)
"""vstack():vertically(row-wise stack)
hstack() : horizontally (column-wise stack)"""
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(np.vstack((arr1,arr2)))#vertical stack #[[1 2 3]
                                              #[4 5 6]]
print(np.hstack((arr1,arr2)))#horizontal stack #[1 2 3 4 5 6]


#SPLITING:dividing one array into multiple sunb-arrays
"""np.split(array,how much parts you want to divde)=equal division of an array
np.hsplit()=horizontal split
np.vsplit()=verticall split"""
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(np.split(arr,2))#[array([10, 20, 30]), array([40, 50, 60])]// array is divide into 2 


#ARRAY COMPATIBILTY:Used to check if shapes of multiple arrays are the same. 
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
print("compatibility shapes:",a.shape==b.shape==c.shape)# compatibility shapes: True

a=np.array([1,2,3])
b=np.array([4,5,6,7])
c=np.array([7,8,9])
print("compatibility shapes:",a.shape==b.shape==c.shape) #compatibility shapes: False