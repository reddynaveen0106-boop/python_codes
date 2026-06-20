# Methods

user = {"id":1, "age": 30, "city": "berlin"}

#Access
#print(user["age"])
#print(user.get("age"))
print(user.get("name", "Unknown"))

#Checks
print("age" in user)
print("name" in user)
#View Objects
print(user.keys())
print(user.values())
print(user.items())
print(user)

#Looping 
for u in user:
    print(u, user[u])

    for key, value in user.items():
        print(key, value)

user = {"id":1, "age": 30, "city": "berlin"}

# Add, Remove, Update
user["name"] = "John"
print(user)
user["age"] = 35
user.update({"age": 40, "city": "Paris"})
print(user)

age = user.pop("salary", "Not Found")
print(user)
print("Removed Item:", age)

user.popitem()
print(user)

# Creation
user = {"id": None,
        "name": None,
        "age": None,
        "city": None
        }

user = dict.fromkeys(["id", "name", "age" , "city"], None)
print(user)
        
        
        
        
        
        