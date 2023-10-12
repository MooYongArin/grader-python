n = int(input())
lst = [n]
while n != 1:
    if n %2 == 0:
        n = n // 2 
    else:
        n = 3*n + 1
    lst.append(n)
if len(lst) > 15:
    for item in lst[-15:]:
        if item != 1:
            print(str(item) + '->',end="")
        else:
            print(item)
else:
    for item in lst:
        if item != 1:
            print(str(item) + '->',end="")
        else:
            print(item)
