a = float(input())
U = 0
L = 1
while True:
    x = a//10
    a = a//10
    U += 1
    if x == 0:
        break
epsilon = 10**(-10)
x = (L + U) / 2 
while abs(a- x**2) > epsilon*max(a,x**2):
    if 10**x < a:
        L = x
    else:
        U = x
    x = (L + U) / 2
print(round(x,6))
