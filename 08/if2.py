#  adadi az karbar begrim va check konim ke aya zoj hast ya fard?
score = int(input('insert one number: '))
#  0 -20 : 0-5--> khail zaeif , 6-10 --> zaeif  , 11-15 --> khob , 16-20 --> khaili khob

#  and , or , not

# if score >= 0 and score <= 5:
#     print('khaili zaeif')
# if score >=6  and score <=10:
#     print(' zaeif')
# if score >= 11 and score <= 15:
#     print('khob')
# if score >=16 and score <= 20:
#     print('khaili khobe')    
#     
    
    
#  if , elif , else 
# if score >= 0 and score <= 5:
#     print('khaili zaeif')
# else:
#     if score >=6  and score <=10:
#     print(' zaeif')
#     else:
#         if score >= 11 and score <= 15:
#         print('khob')
#         else:
#             if score >=16 and score <= 20:
#                 print('khaili khobe')    


#  if , elif , else 
if score >= 0 and score <= 5:
    print('khaili zaeif')
elif score >=6  and score <=10:
    print(' zaeif')
elif score >= 11 and score <= 15:
    print('khob')
else:
    print('khaili khobe')    
