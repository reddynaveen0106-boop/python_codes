# Copying 
import copy
matrix = [
    ['a', 'b'],    # Row 0
    ['c', 'd'],    # Row 1
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:       ', matrix_copy)

import copy
original = [
    ['a', 'b'],   # Row 0
    ['c', 'd'],   # Row 1
]
#Assigment
copy1 = original
print("Same object?", original is copy1, "\n")

#Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy, "\n")
print("Shared lists?", original [0] is copy2[0], "\n")

#Deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3 [0], "\n")
