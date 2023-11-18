

score = int(input('insert one number: '))
if score < 0 or score > 20:
    print('adad dar range score nist plz adad bin 0,20 vared konid')
else:    
    if score >= 0 and score <= 5:
        print('khaili zaeif')
    elif score >=6  and score <=10:
        print(' zaeif')
    elif score >= 11 and score <= 15:
        print('khob')
    else:
        print('khaili khobe')    

