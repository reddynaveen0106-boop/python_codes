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