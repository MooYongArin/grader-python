n = int(input())
lst = []
for i in range(n):
    x = int(input())
    if i %2 == 0:
        lst.append(x)
    else:
        lst.insert(0,x)

k = [int(e) for e in input().split()]
for i in range(len(k)):
    if n%2 == 0:
        if i %2 == 0:
            lst.append(k[i])
        else:
            lst.insert(0,k[i])
    else:
        if i %2 != 0:
            lst.append(k[i])
        else:
            lst.insert(0,k[i])

i = 0
while True:
    x = input()
    if x == '-1':
        break
    x = int(x)
    if (n+len(k)) %2 == 0:
        if i %2 == 0:
            lst.append(x)
        else:
            lst.insert(0,x)
    else:
        if i %2 != 0:
            lst.append(x)
        else:
            lst.insert(0,x)
    i += 1
print(lst)