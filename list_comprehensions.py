domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [
    d.lower().replace('www.', '')
    # Data Transfotmation
    for d in domains
    if '.' in d
    # Data Filtering
]

print(cleaned)