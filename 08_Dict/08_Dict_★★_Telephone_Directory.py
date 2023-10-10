dct = dict()
dct_2 = dict()

N = int(input())

for i in range(N):
    name,surname,tel = input().split()
    full_name = str(name) + " " + str(surname)
    dct[full_name] = tel
    dct_2[tel] = full_name

M = int(input())
ans = []
for i in range(M):
    find = input()
    if find in dct:
        ans.append([find,dct[find]])
    elif find in dct_2:
        ans.append([find,dct_2[find]])
    else:
        ans.append([find,"Not found"])
for item in ans:
    print(item[0], '-->' ,item[1])