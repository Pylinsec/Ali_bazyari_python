# tuple --> method --> count(),index()
# range(start,stop,step)
# print(tuple(range(10,21)))
# print(list(range(10,21)))

t1 = (20, 61, 82, 13, 104, 15, 13, 170, 13, 1.9, 20.345)
# count(chiz)> shomaresh tedad chiz dar tuple 
# print(t1.count(13))
# print(t1.count(103))

# index(chiz)--> dar soorat vojood shomareh khane avalin itemi ke bahash match hast miareh 
# print(t1.index(13))

# soal --. revesh pida kardan temam index haye yek item
t2 = list(t1)
# print(t2)
# print(t2.index(13))
for item in t2:
    if item == 13:
        ind = t2.index(item)
        t2[ind] = 'a'
        print(ind)
