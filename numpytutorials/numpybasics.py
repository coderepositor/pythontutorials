#numpy - Numerical python library, it provides more speed, fewer loops, clearer code
#better quality. It is used for operations on multidimensionaly array. Majorly
#used in the field of data science

import numpy as np
"""
digits = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

print(digits)
"""
"""print(digits.shape) #size of an array
row_vector = digits[:,np.newaxis]
print("digits", row_vector)
col_vector = digits[np.newaxis:]
print("digits", col_vector)

"""
#Vectorization - It is the process of performing the same operation in the
#sameway for each element in the array. This removes for loop from your code
#Broadcasting - It is the process of extending two arrays of different shape
#and figuring out how to perform a vectorized calculation between them.

"""
CURVE_CENTER = 80
grades = np.array([72,35,64,88,51,90,74,12])
average = grades.mean();
print(average)
change = CURVE_CENTER - average
print(change)
def curves(grades):
    average = grades.mean();
    #print(average)
    change = CURVE_CENTER - average
    new_grades = grades + change #vectorization
    return np.clip(new_grades,grades,100) #broadcasting

print(curves(grades))
"""
"""
tempratures = np.array([29.3,42.1,18.8,16.1,38.0,12.5,12.6,49.9,38.6,
                        31.3,9.2,22.2]).reshape(2,2,3)

print(tempratures.shape)
print(tempratures)

print("*" * 60)
print(np.swapaxes(tempratures,1,2))
"""
"""
batting_averages = np.array([
    [50,30,70,10],
    [20,60,90,70],
    [100,90,100,80],
    [40,30,20,0]
    ])
print("Size of an array: ",batting_averages.shape)
print("Maximum Average: ", batting_averages.max())
print("Maximum Average Column: ", batting_averages.max(axis=0))
print("Maximum Average Row: ", batting_averages.max(axis=1))
"""
"""
numbers = np.linspace(5,51,24,dtype=int).reshape(4,6)
print(numbers)
"""
"""
nums = np.arange(32).reshape(4,1,8)
print(nums)
nums_1 = np.arange(48).reshape(1,6,8)
print(nums_1)
print("*" * 60)
print(nums + nums_1)
"""
"""
arr1 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr1)
print("*" * 60)
arr2 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr2)
sum_of_2_arrays = arr1+arr2
print("Sum of arrays")
print(sum_of_2_arrays)

prod_of_2_arrays = arr1*arr2
print("product of arrays")
print(prod_of_2_arrays)
"""
square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
    ])
"""for i in range(4):
    print(square[:,i].sum()==34)
    print(square[i,:].sum()==34)
"""
#print(square[:2,:2])
#print(square[2:,2:])

numbers = np.linspace(5,50,24,dtype="int").reshape(4,-1)
#print(numbers)
print("-"*60)
#mask = numbers%5==0 #vectorized boolean computation
#print(mask)

#filtering
#print("all the values divisible by 5 ", numbers[mask]) #converting a resultant array into single dimension
#print("all the values divisible by 8 ", numbers[numbers%8==0])

#print(numbers.T) #Tranposing
#print("Horizontal Sorting", np.sort(numbers,axis=0))
#print("Vertical Sorting", np.sort(numbers,axis=1))


a = np.array([[4,8],[6,1]])
b = np.array([[3,5],[7,2]])

#print(np.concatenate((b,a)))#merging two array
#print(np.concatenate((b,a),axis=None))#merging two array and converting it into single dimension array
#print(np.hstack((a,b)))#horizontal merging of 2 or more arrays
#print(np.vstack((a,b)))#vertical merging of 2 or more arrays

stock_prices = np.random.random((30,10))
print("stock_prices")
print(stock_prices*10) 

































































