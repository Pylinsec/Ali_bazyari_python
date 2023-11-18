# agar n adadi zoj bashad 
n=8
for i in range(n):
    for j in range(n):
        if (i == 3 and j == 3) or(i == 3 and j == 4) or(i == 4 and j == 3) or(i == 4 and j == 4) :
            print('O',end=' ')
        else:
            print('X',end=' ')
    print()
    
print(''.center(130,'='))
print(''.center(130,'*'))
print(''.center(130,'='))

n=32


for i in range(n):
    for j in range(n):
        t1 = ((i == (n-1) // 2) and (j == (n-1) // 2))
        t2 = ((i == (n-1)// 2) and (j == n // 2))
        t3 = ((i == n // 2) and (j == (n-1) // 2))
        t4 = ((i == n // 2)  and (j == n // 2)) 
        if  t1 or t2 or t3 or t4:
            print('O',end=' ')
        else:
            print('x',end=' ')
    print()