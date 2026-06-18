#Skip weekends in calendar loop
days = ['Mon', 'Sun', 'wed', 'Tue']
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(F'Workday: {day}')