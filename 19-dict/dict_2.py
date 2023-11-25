# dictinary ---> dict={key:value,}
car1 = {'brand':'pejout','year':94,'country':'france'}
# access to one item 
print(car1['brand'])
print(car1.get('brand'))
# access keys
print(car1.keys())
# access values
print(car1.values())
for value in car1:
    print(car1.get(value))

for value in car1.keys():
    print(car1.get(value))

for value in car1.keys():
    print(car1[value])

# car1.items()--> [(key,value)]
print(car1.items())

for item in car1.items():
    print(item[1])