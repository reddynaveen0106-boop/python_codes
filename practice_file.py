score = 50 
#if score >= 90:
#    print("A")
#elif score >= 80:
#else:
#    print("F")

grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)
country = "India        "
match country: 
    case "United States":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unkown country")

# Email must contain a '.' and '@' 
# Email must contain exactly one '@' symbol
# Email must end with '.com', '.org', or '.net'
# Email must not be longer than 254 characters
# Email must start and end with a letter or digit 
email = " reddynaveen@gmail.com "
# Clean the string 
email = email.strip()
# Email must not be empty
if email == "":
    print("Email cannot be empty.")
#Email must contain a '.' and @ 
if not('.' in email and '@' in email):
    print("Email must contain . and @")
# Email must end with '.com', '.org', '.net')
if not email.endswith((',com', '.org', '.net')):
    print("Email must end with '.com'")
    # Email must not be lomger than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
# Email must start and end with a letter or digit
if not (email[0].isalnum() and email [-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")
