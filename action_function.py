'''# Task: store applications log messages in a file
def write_log(message):
    with open(r"C:\Main\Python\app.log", "a") as file:
        file.write(message + "\n")

write_log("App Started")
write_log("user logged in")
write_log("App started")'''

# Task: Clean an email and split it into username and domain
'''def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username, domain = cl_email.split("@")
    return {"username": username,
            "domain": domain}

print(clean_and_split_email("SARA@gMAil.com"))'''
# Task: Check if a password meets the minimum length of 8 characters
'''def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("123456"))
print(is_valid_password("123456987"))'''
# Task: check if email has a basic valid format

def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("sararagamol.com"))