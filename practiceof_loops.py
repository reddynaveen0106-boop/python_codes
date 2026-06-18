# 3 attempts
# Yes within three attempts -> "Glad we're on the same page"
# Otherwise "3 strikes. you are out"
attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts +=1
else:
    print("3 strikes. You're out!")
