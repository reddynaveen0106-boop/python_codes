names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f'Name = {name}')