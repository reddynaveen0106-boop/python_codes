# append - this method used to add the content at the end of the previous data
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
print(letters)
# Insert - add the data at any point

letters = ['a', 'b', 'c']
letters.insert(0, 'x')
letters.insert(3, 'y')
print(letters)

# Adding the data in the 2d matrix
matrix = [
    ['a', 'b', 'c'],      # Row 0
    ['d', 'e', 'f'],      # Row 1
    ['g', 'h', 'i']       # Row 2
]
matrix.append(['x', 'y', 'z'])
matrix.insert(0, ['a', 'a', 'a'])
print(matrix)

# How to remove the data?
letters = ['a', 'b', 'c']
letters.clear()
print(letters)

letters = ['a', 'b','a']
letters.remove('a')
letters.remove('a')
print(letters)

letters = ['a', 'b','a']
letters.pop(2)
print(letters)
letters.pop(1)
print(letters)

letters = ['a', 'b', 'c']
removed = letters.pop()
print(letters)
print('Removed Item:', removed)

# Removing the stuff in matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix.remove(['a', 'b', 'c'])
matrix.pop()
print(matrix)

# Updating the value
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
letters = 'z'
print(letters)
print(type(letters))
print(letters)
print(type(letters))