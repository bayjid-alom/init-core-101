"""
In Python, a sequence data type is an ordered collection of items
where each element is associated with a specific position or integer index [8, 10].
These types allow for efficient storage, access, and manipulation of multiple values
within a single object [8, 11].

Sequence Types:	list, tuple, range
"""

# list[] -- mutable

li = ["Apple", "Ball", "Cat", "Dog", "Egg", "Football"]
print("List is:", li)

li[4] = "Elephant"
print(li)
print(type(li))       #<class 'list'>


# Tuple()  -- immutable

my_tuple = ("Red", "Pink", "Yellow")
print(my_tuple)

numbers = (10,20,30,40,50)
print(numbers)
print(type(numbers))


# range type data
ran = range(6)    #0-5 = total 6
for i in ran:
    print(i)

numbers_1 = range(20)
for i in numbers_1:
    print("(0-19) :", i)



