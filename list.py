# Crreate list
empty = []
letters = ['a', 'b', 'c']
numbers = [1 , 2, 3]
mixed = [1, 'a', True, None]
print(mixed)
print(type(letters))
empty = list()
print(empty)

letters =list('Python')
print(letters)

numbers = list(range(5))
print(numbers)
# Create Lists
empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = [1, 'a', True, None]

matrix = [['a', 'b', 'c'],
           ['d', 'e', 'f'],
           ['1', '2', '3']]

print(matrix)
print(type(matrix))

# Access & Read

lst = ['a', 'b','c', 'd']
print(lst)
print(lst[0])
print(lst[-2])

# Access & Read
matrix = [['a', 'b', 'c'],   #Row 0
           ['d', 'e', 'f'],  # Row 1
           ['g', 'h', 'i']   # Row 2
]

print(matrix)
print(matrix[2])
print(matrix[-1])
print(matrix[-1],) , print(matrix[-2]), print(matrix[-3])
print(matrix[0 ][0])

# slicing
lst = ['a','b','c', 'd']
print (lst[:])
print(lst[2:])

# Slicing in the matrix
matrix = [['a', 'b', 'c'],   #Row 0
           ['d', 'e', 'f'],  # Row 1
           ['g', 'h', 'i']   # Row 2
]

print(matrix[0:2])
print(matrix[1:])
print(matrix[2][:2])

person = ['Maria', 29, 'Data Engineer', 'Spain' , 'hyd']

name, *_  = person

print(name)
