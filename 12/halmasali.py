import math
print(math.factorial(4))
adad = int(input('adadi vared konid: '))
print(adad)

# ozve khonsa jam: 0
# ozve khonsa amal zarb: 1
# ozve khonsa string: ''

fact =1
for i in range(1,adad+1):
    fact *= i

print(f"factorial {adad} is ",fact)
