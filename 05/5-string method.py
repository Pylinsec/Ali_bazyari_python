#  string method --> function ya tabe


name = 'ali bazyari age '
name2 = 'ALI BAZYARI'
name3 = 'aLI baZyarI'

# title()--> avali harf az temam kelamat jomleh agar koochak bood capital mikone
print(name.title())
print(name.capitalize()) # dar in halat feghat avalin harf az avali  keleme capital mishe

# upper()--> capital mikone
print(name.upper())

# casefold() , lower()  -> temam hooroof koochak mikone
print(name2.lower())
print(name2.casefold())


# swapcase  --> agar capital bood lower mikone agar lower bood capital mikone
print(name3.swapcase())

# replace(sub1,sub2) --> agar sub1 dar string bood ba sub2 replace mikona
print(name.replace('ali','qoli'))
print(name.replace('h','qoli')) # agar nebood etefaghti nemioftad

# center()--> markaz gera hast
print('bazyari'.center(20,'*'))
print(' start '.center(120,'*'))
print(''.center(100,'-'))
print('ali bazyari')
print(''.center(100,'-'))
print(' end '.center(100,'*'))



