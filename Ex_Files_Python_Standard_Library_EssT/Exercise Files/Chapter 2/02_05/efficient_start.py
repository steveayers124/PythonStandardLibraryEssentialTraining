# The array type can hold homogeneous data types and operate
# on them more efficiently while using less memory

from array import array

# TODO: Create an array of integer numbers
ar = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
# 'i' is for integer data https://docs.python.org/3/library/array.html?highlight=array
print(ar)
print(ar.typecode)
# integer data takes 4 bytes per item
print("Array 1 item size", ar.itemsize)

# TODO: Add additional items to the array
ar.insert(0,0)
ar.append(22)
ar.extend([24,26,28])
print(ar)

# TODO: iterate over the array content like any other list
for i, elem in enumerate(ar):
    ar[i] = elem * 2
print(ar)

# TODO: Try to add a non-integer number to the array
# ar.insert(0, 1.25)
### This failed with error "TypeError: integer argument expected, got float"

# TODO: Create an array to hold bytes instead of ints
arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])
print(arr2)
print(arr2.typecode)
print("Array 2 item size: ", arr2.itemsize)

# TODO: try to add an item that's out of range
# (bytes can only be 0 to 255)
# arr2.append(256)
### This failed with the error "OverflowError: unsigned byte integer is greater than maximum"

# TODO: Convert an array to a list
list1 = arr2.tolist()
print(list1)
# list1.(256)
# print(list1)
