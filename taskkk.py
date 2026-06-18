emails = [
    'data@gmail.com',
    'baraa@oulook.de',
    'DROP TABEL USERS',
    'maria@gmail.com'

]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email: {email}')
   