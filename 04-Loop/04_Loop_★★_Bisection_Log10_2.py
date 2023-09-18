a = float(input())
U = 0
L = 0
while True:
    x = a//10
    a = a//10
    U += 1
    if x == 0:
        break

print(U)