#  list = [],
#  mesal
[1,2,3,4,5]
[True,False,True,False]
['ali','bazyari','dahom','student']
[2.3,3,4,5.6]
[1,2,'ali',True,[3,3,4,45,55,5,5,5],4.5]

# --> orderd ( jay item ha mohem hast)
l1 = [1,2]
l2 = [2,1]
# print(hex(id([1,2])))
# print()
# print(hex(id([1,2])))
# print(l1 is l2)
# print([1,2] is [1,2])
print(l1 == l2)

#allow duplicate (item tekrar qebool mikonad) ,
l3 = [1,1,1,2]
print(l3)
#changeable (avaz kardan)
l3[1]='ali bazyari'
print(l3)



# type() --> moshakhas konandeb no sakteman
print(type('ali bazyari'))
print(type(l3))


#  len() --> bedast avardan tedad item ha
print(len(l3))