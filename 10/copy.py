#  copy
colors = ['red','blue','red','green','black','white','pink','purple']
colors2 = colors
colors.pop()
colors.insert(3,'piaz')
print(colors2)

# copy()
colors = ['red','blue','red','green','black','white','pink','purple']
colors2 = colors.copy()
colors.pop()
colors.insert(3,'piaz')
print(colors2)