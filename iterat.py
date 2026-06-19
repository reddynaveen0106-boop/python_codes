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

letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = ['naveen', 'reddy', 'Kumar']
for n in map(str.strip, names):
    print(n)