#  split() --> list besaz [,,]
name = 'Ali*Bazyari*at*age *15'
print(name.split()) # agar chizi nedim be tor pishfarz bar asas space mishekine v list misaze
print(name.split('Ali'))
print(name.split('Ali2')) # agar nabood list az kol string misazeh ba yek ozv
print(name.split('*',2)) # shekastan bar asas tedad * 
print(name.split('*',3))
print(name.split('*',30))


