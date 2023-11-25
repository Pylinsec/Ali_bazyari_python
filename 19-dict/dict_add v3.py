car1 = {'brand':'pejout','year':94,'country':'france'}
# how to change dictionary --> add , remvoe , change

# change , add  --> feghat dar values
car1['country']= 'iran'
print(car1)
# update() --> chand item avaz she
car1.update({'brand':'ford','year':'1998','color':'red'})
print(car1)
car1['euro4'] = False
print(car1)

#  how to add one dictionary to another dictionary
car2 = {'model':'lx'}
car1.update(car2)
print(car1)
car2.update(car1)
print(car2)