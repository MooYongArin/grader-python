str1 = input().lower()
str2 = input().lower()

dct1 = {}
dct2 = {}
for item in str1:
    if 'a'<=item<='z':
        if item in dct1:
            dct1[item] += 1
        else:
            dct1[item] = 1
for item in str2:
    if 'a'<=item<='z':
        if item in dct2:
            dct2[item] += 1
        else:
            dct2[item] = 1

lst1 = []
lst2 = []
for item in dct1:
    if dct1[item] > dct2[item]:
        x = dct1[item] - dct2[item]
        if x>1:
            lst1.append(['remove',item,str(x)+"'s"])
        else:
            lst1.append(['remove',item,x])
    elif dct1[item] < dct2[item]:
        x = dct2[item] - dct1[item]
        if x>1:
            lst2.append(['remove',item,str(x)+"'s"])
        else:
            lst2.append(['remove',item,x])
check = True
if lst1 == []:
    lst1.append("None")
    check = False
if lst2 == []:
    lst2.append("None")
    check = True
    
print(str1)
for item in lst1:
    if item == 'None':
        print(' - None')
        break
    print(' - ',end="")
    for i in item:
        print(str(i) + ' ',end="")
    print()
print(str2)
for item in lst2:
    if item == 'None':
        print(' - None')
        break
    print(' - ',end="")
    for i in item:
        print(str(i) + ' ',end="")
    print()