# copy() dictionary
car = {'brand':    'ford',
        'year':    '1998',
        'country': 'iran',
        'color':   'red',
        'euro4':    False, 
        'model':    'lx'} 

# in revesh monaseb copy nist
# car1 = car
# car1['sokht']= 'benzin'
# print(car)

# copy()
car1 = car.copy()
car1['sokht']= 'benzin'
print(car)
print(id(car),id(car1))