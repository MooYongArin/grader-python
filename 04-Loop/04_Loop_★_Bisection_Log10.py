a = float(input())
L = 0.0
U = a
epsilon = 10**(-10)
x = (L + U) / 2 

while abs(10**x - a) > epsilon:
    if 10**x < a:
        L = x
    else:
        U = x
    x = (L + U) / 2

print(round(x,6))