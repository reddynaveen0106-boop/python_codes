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

letters = ['a', '', 'b',None, 'c', False]
print(list(filter(bool, letters)))

# lambda
multiple = lambda x: x*2
print(multiple(2))

add = lambda x, y: x + y
print(add(1,2))

check = lambda i: i in "python"
print(check('z'))

# Lambda + Map

price = ['$12.58','$123.276', '123.456']
print(list(map(lambda p: float(p.replace("$", '')), price))) 
               #2->put in Lambda  #->1 Data transformation 
           #3 Map the function to iterartor to manipulate my data, All these things are related to abouve line 37 

           
# Lambda + filter 

price = [120,30,300,80] 

print(list(filter(lambda p: p >= 100, price)))

students = [['Maria', 85],
            ['kumar', 90],
            ['Max', 60]]
print(students [0][1] > 70)

print(list(filter(lambda row: row[1] > 70, students)))
