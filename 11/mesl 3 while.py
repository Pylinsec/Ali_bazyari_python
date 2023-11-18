#  adad ye kochaktar az 100000 ke ham bar 5 ham bar 7 , ham bar 3 bakhpezi hast chap konad.

num = 1
count = 0
while num <= 100000:
#     if num % 3 ==0 and num %5 == 0 and num % 7 ==0:
    if num % 105 == 0:    
        print(num,end=' ')
        count +=1
        num += 1
    else:
        num +=1
print(count)