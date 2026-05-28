# Binary Types:	bytes, bytearray, memoryview

"""


bytes (immutable): range (0-255)
The bytes() function returns a bytes object.
It can convert objects into bytes objects, or create empty bytes object of the specified size.

bytearray: (mutable) range 0-256
"""

# binary type data - bytes

list = [10,20,30,40,50]
X = bytes(list)
print(type(X))    #<class 'bytes'>


# binary type data - byteArray
# mutable

list_2 = [25,50,75,100]
Y = bytearray(list_2)

Y[1]= 100

print(list_2)
print(Y[1])
print(type(Y))     #<class 'bytearray'>



