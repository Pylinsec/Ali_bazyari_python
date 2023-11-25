# dictinary ---> dict={key:value,}
car1 = {'brand':'pejout','year':94,'country':'france'}
car2 = {'brand':'pejout','country':'france','year':94}

# changeable , not allowed duplicate , orderd
# test order boodan 
print(car1 is car2)

car2 = {'brand':'pejout','country':'france','country':'france','year':94,'year':94,'year':94}
print(car2)

print(list(car1.keys()))
print(list(car2.keys()))
# type
print(type(car1))
# len()
print(len(car2))
