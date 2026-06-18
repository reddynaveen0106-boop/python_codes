# Combining the lists
letters = ['a', 'b' ,'c']
numbers = [1,2,3]
comb = letters + numbers
print(comb)
print(letters * 2)

# Combining
letters = ['a', 'b', 'c']
numbers = [1,2,3,4,"hi"]
comb = list(zip(letters, numbers, "hi"))
print(comb)

ids = [101,102,103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))