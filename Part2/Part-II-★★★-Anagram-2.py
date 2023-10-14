in_str1 = input()
in_str2 = input()
str1 = in_str1.lower()
str2 = in_str2.lower()

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
    if item not in dct2:
        x = dct1[item]
        if dct1[item] > 1:
            lst1.append(['remove',x,str(item)+"'s"])
        else:
            lst1.append(['remove',x,item])
for item in dct2:
    if item not in dct1:
        x = dct2[item]
        if dct2[item] > 1:
            lst2.append(['remove',x,str(item)+"'s"])
        else:
            lst2.append(['remove',x,item])
for item in dct1:
    if item in dct2:
        if dct1[item] > dct2[item]:
            x = dct1[item] - dct2[item]
            if x>1:
                lst1.append(['remove',x,str(item)+"'s"])
            else:
                lst1.append(['remove',x,item])
        elif dct1[item] < dct2[item]:
            x = dct2[item] - dct1[item]
            if x>1:
                lst2.append(['remove',x,str(item)+"'s"])
            else:
                lst2.append(['remove',x,item])

check1 = True
check2 = True
if lst1 == []:
    check1 = False
if lst2 == []:
    check2 = False

# เรียงตัวอีกษร

for item in lst2:
    item.insert(0,item[2][0])
lst2.sort()
for item in lst2:
    item.pop(0)
for item in lst1:
    item.insert(0,item[2][0])
lst1.sort()
for item in lst1:
    item.pop(0)

print(in_str1)
if check1:
    for item in lst1:
        if len(item) == 3:
            print(' -',item[0],item[1],item[2])
        elif len(item) == 4:
            print(' -',item[0],item[1],str(item[2])+"'s")
else:
    print(' -','None')
print(in_str2)
if check2:
    for item in lst2:
        if len(item) == 3:
            print(' -',item[0],item[1],item[2])
        elif len(item) == 4:
            print(' -',item[0],item[1],str(item[2])+"'s")
else:
    print(' -','None')

