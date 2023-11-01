dct1 = {}
for i in range(int(input())):
    x,y = input().split()
    dct1[x] = int(y)
lst = []
for i in range(int(input())):
    x = input().split()
    x[0],x[1] = float(x[1]),x[0]
    lst.append(x)
lst = sorted(lst,reverse=True)
dct2 = {}
for item in lst:
    for test in item[2:]:
        if dct1[test] > 0:
            dct2[item[1]] = test
            dct1[test] -= 1
            break
for item in sorted(dct2):
    print(item, dct2[item])
