# Unpacking the lists
person = ['Maria', 29, 'Data Engineer', 'Spain' , 'hyd']
#name = person [0]
#age = person [1]
#role = person[2]
#country = person[3]

name, age, role, country , city  = person

print(name)
print(age)
print(role)
print(country)
print(city)

# use *
person = ['Maria', 29, 'Data Engineer', 'palce of birth', 'Spain' , 'hyd']
name, *details , city  = person
print(name)
print(details)
print(city)

person = ['Maria', 29, 'Data Engineer', 'Spain' , 'hyd']

name, *details = person
print (person)

person = ['Maria', 29, 'Data Engineer', 'Spain' , 'hyd']

name, _ , role, _, city = person

print(name)
print(age)
print(role)
print(country)
print(city)