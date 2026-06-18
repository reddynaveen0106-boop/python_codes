for x in range(3): # outer loop
    for y in range (2): # inner loop
        for z in range(2):
            print(f"({x}, {y}, {z})")

# Concepet is to pair the each colours for each gradient
colors = ['red', 'blue','green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
years = [2026,2027]
months = ['Jan', 'Feb']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m},{d}.csv')


# SELECT count(*) FROM customers where id IS NULL;
tables = ['customers', 'ordrers', 'products', 'prices', 'ride', 'hide', 'tide', 'routh']
columns = ['id', 'create_date' , 'moon', 'rain', 'sun']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')



