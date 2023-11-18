t1 = ((10, 20,23,12), (30,11,34,45, 56, 45), (81,-1,-23, 80, 32),(3,12,4),(1,),(34,54))

new =[]
for item in t1:
    sum1 = 0
    for i in item:
        sum1 += i
    new.append(sum1/len(item))

# print(new)    
# revesh 2
t1 = ((10, 20,23,12), (30,11,34,45, 56, 45), (81,-1,-23, 80, 32),(3,12,4),(1,),(34,54))
new1 = []
for item in t1:
    print(sum(item))
    new1.append(sum(item)/len(item))
print(new1)    


