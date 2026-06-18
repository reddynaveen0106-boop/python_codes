items = [1,3,4,7]
for i in items:
    print(i)
else: 
    print ("Loop is completed")
# Check for even number
items = [1,3,4,7]
for i in items:
    if i % 2 == 0:
        print("Even number is found-R", i)
        break
else:
    print ("Loop is completed")

# For the Fruit names that contains consonants
fruits = 'Apples' 'oranges' 'aeio'
for f in fruits:
   has_consonant = any(char.isalpha() and char.lower() not in 'aeiou'for char in fruits)
   if has_consonant:
       print(fruits)
names = ['kamara' , 'Tuba', 'Naveen' , 'Mounika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are avaiable")

names = ['nsaveen','reddy','ravci']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print ("orey ep" \
    "orey ep")
files = ['data1.csv,'


             'report.pdf '
             
             'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file}is not a csv')
        break
else:
    print('all files are csv')

    