a = float(input('insert num2: '))
b = float(input('insert num3: '))
c = float(input('insert num3: '))
d = float(input('insert num3: '))

if a >= b:
    max1 = a
else:
    max1 = b
    
if c >= d:
    max2 = c
else:
    max2 = d
    
if max1 >= max2:
    print('max is ',max1)
else:
    print('max is ',max2)