days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

days_iter = iter(days)

print next(days_iter)
print next(days_iter)
print next(days_iter)
print next(days_iter)

#iterating over file

with open('array_indexing.txt','r') as f:
    for line in iter(f.readline,''):
        print line