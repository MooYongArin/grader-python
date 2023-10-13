a = float(input())
L = 0
U = 0
copy_a = a
while True:
    x = copy_a//10
    copy_a = copy_a//10
    U += 1
    if x == 0:
        break

x = (L + U) / 2 
while abs(a- 10**x) > 1e-10*max(a,10**x):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (L + U) / 2

print(round(x,6))
