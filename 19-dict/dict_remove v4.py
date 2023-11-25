car = {'brand':    'ford',
        'year':    '1998',
        'country': 'iran',
        'color':   'red',
        'euro4':    False, 
        'model':    'lx'}

# pop , popitem , del , clear
# car.pop(key)--> ham key , ham value hazf mishe
car.pop('color')
print(car)

# popitem() --> akharin item dictionary ra hazf mikonad
car.popitem()
print(car)

# hazf kamel data ha 
car.clear()
print(car)

# del khode sakhtemn hazf mikone
del car
print(car)