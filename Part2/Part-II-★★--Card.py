x = input()
lst = []
dct={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
dct2={'C':1,'D':2,'H':3,'S':4}
for i in range(0,len(x)-1,+2):
    y = x[i]+x[i+1]
    lst.append(y)
ans = []
i = 0
while i < (len(lst)-1):
    if dct[lst[i+1][0]] != dct[lst[i][0]]:
        temp = dct[lst[i][0] ]- dct[lst[i+1][0]]
        if temp > 0:
            temp = '+'+ str(temp)
        ans.append(temp)
    else:
        if dct2[lst[i][1]] != dct2[lst[i+1][1]]:
            temp = dct2[lst[i][1]]- dct2[lst[i+1][1]]
            if temp > 0:
                temp = '+'+ str(temp)
            ans.append(temp)
        else:
            ans.append(0)
    i += 1
for item in ans:
    print(item,end="")