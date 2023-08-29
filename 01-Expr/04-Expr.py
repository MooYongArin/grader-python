import math

kg = float(input())
cm = float(input())

print((math.sqrt( kg*cm ))/(60))
print((0.024265)*(kg**0.5378)*(cm**0.3964))
print((0.0333)*((kg)**((0.6157)-(0.0188*math.log(kg,10))))*(cm**0.3) )