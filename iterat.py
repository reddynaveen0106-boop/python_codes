letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)
# Enumerate
letters = ['a', '', '']
print(list(enumerate(letters, start = 1)))
for index, value in enumerate(letters):
    print(index, value)