text = '''
Recently protect day near nation.
Listen leave security card thing often various.
'''
# lower() , casefold()  : capital to lower
print(text.casefold())
print(text.lower())

# upper() , capitalize() , title()
print(text.upper()) # upper --> lower to capital
print(text.title()) # har aval temam kelemat be capital tabdil mishe
text1 = ' this is for test'
print(text1.capitalize()) # avalin harf jomleh be capital 


# find(qoli) , index(qoli) --> bargardandan shomerh khane qoli
# agar bood agar nebood dar index error mide vali dar find -1 barmigardand
print(text.find('protect')) # index avalin harf 'protect' yani 'p'
print(text.index('protect'))# index avalin harf 'protect' yani 'p'

# count(qoli,start,end) --> tedad qoli ha ra mishomre agar nebood 0
print(text.count('e'))
print(text.count('l',2,10)) # range(2,10) yani az khane 2 ta 9 ra jostejoo kon

# replace(qoli1,qoli2) --> dar soorat yaftan qoli1 bejash qoli 2 mizare
# fehat avalin qoli1 agar payda kard ba qoli2 jabeja mikone
print(text.replace('day','*week*'))




