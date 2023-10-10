N = int(input())
dct = {}
dct_2 = {}
for i in range(N):
    nickname,realname = input().split()
    dct[nickname] = realname
    dct_2[realname] = nickname

M = int(input())
ans = []
for i in range(M):
    key = input()
    if key in dct:
        ans.append(dct[key])
    elif key in dct_2:
        ans.append(dct_2[key])
    else:
        ans.append("Not found")

for item in ans:
    print(item)


