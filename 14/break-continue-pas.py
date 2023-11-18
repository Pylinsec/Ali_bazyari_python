# break --> agar shart true bood az loop mipare biroon
for i in range(100):
    if i > 50:
        break
    print(i,end='')
print('ali bazyari')    
# continue --> agar shart true bood mire adameh loop
for i in range(51):
    if i % 2 == 1:
        continue
    else:
        print(i , end='-->')
  
# pass --> mizarim error negireh  badan biam codesh benevisam
if 4 > 3:
    pass