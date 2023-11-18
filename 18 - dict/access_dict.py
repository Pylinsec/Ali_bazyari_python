ali = {'name':'Ali','lastname':'Bazyari','age':15,'city':'jam','address':'shahrak 372'}

# access to keys
print(ali.keys())
# for item in ali:
# for item in ali.keys():
#     print(item)
# ======================================================
# access to values
print(ali.values())
# for item in ali.values():
#     print(item)
# =======================================================
# all keys and values
# print(ali) 
# tuple barmigardanad
for item in ali.items():
    # print(item)
    print(item[0])

print(ali.items())  
# =======================
print('reza' not in ali)
print('name' in ali.keys())
print('Ali' in ali.values())