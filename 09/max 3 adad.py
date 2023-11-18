#  max 3 addad
a = float(input('insert num1: '))
b = float(input('insert num2: '))
c = float(input('insert num3: '))

# revesh 1 
# if a >= b:
#     if a >= c:
#         print('max is',a)
#     else:
#         print('max is',c)
# else:
#     if b >=c:
#         print('max is' ,b)
#     else:
#         print('max is ',c)
        
# --------------reveshg dovom
if a >= b and a >= c:
    print('max is ',a)
elif b > a and b >= c:
    print('max is ',b)
else:
    print('max is ',c)
    
# revesh 3
print('max is ',max(a,b,c))
    
    