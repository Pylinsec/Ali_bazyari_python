lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2),('a','b','c')]

new =[]
for item in lst_tuples:
    new.append(list(item))

# print(new)    

# [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2], ['a', 'b', 'c']]
#  list of lists --> tuple of tuples 

l = [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2], ['a', 'b', 'c']]
# make tuple of tuples
n = []
for item in l:
    n.append(tuple(item))
    # print(n)   
t_n = tuple(n)
print(t_n)