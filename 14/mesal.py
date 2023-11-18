# 1 1 1 1 
for i in range(4):
    print('1',end=' ')


print()
# 1 2 3 4
for i in range(1,5):
    print(i,end=' ')

print() 

# 1 2 3 4  
# 1 2 3 4  
# 1 2 3 4  
# 1 2 3 4  
for i in range(4): 
    for j in range(1,5):
        print(j,end=' ')
    print()   


print()
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4  
for i in range(4): 
    for j in range(1,5):
        print(i,end=' ')
    print()    