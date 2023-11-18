#  remove
colors = ['red','blue','red','green','black']

# hazf az tarig khode meqdar: remove --> list1.remove('red') --> khode item ra migire jostejoo mikone agar bood avalin gozine ke bahash match shod hazzf mikonad

colors.remove('red')
print(colors)


# hazf az tariq index --> pop()
colors.pop() # --> hazf az tahe list
print(colors)

colors.pop(2)
print(colors)

#  mesal --> hazf range[2,6]
colors = ['red','blue','red','green','black','white','pink','purple']
#  revesh 1
# colors[2:6]=''
#  revesh 2
# colors.pop(3)
print(colors)


#  clear() --> khane khali kardan
colors.clear()
print(colors)

#  del  -> hazf sakhteman 
del colors
print(colors)