#  changeable

names = ['ali','taha','bardia','som','sajjad','qoli']
#  tagiir dar yek item
names[2] = 'jamshid'
print(names)

#  tagiir dar range item ha
names[2:4] = 'havij','levashak','pedram','rerzvam'
print(names)


names = ['ali','taha','bardia','som','sajjad','qoli']
#  insert(index,value) --> value dar khame be shomereh index bezar
names.insert(3,'morteza')
print(names)
names.insert(-1,'laboo')
print(names)


#  names.append(value) --> value mizare tahe list
names.append('hendooneh')
print(names)