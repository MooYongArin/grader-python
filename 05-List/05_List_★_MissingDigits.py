ten = ['0','1','2','3','4','5','6','7','8','9']
ans = []
x = input().strip()

for item in ten:
    if item not in x:
        ans.append(item)

if ans == []:
    print("None")
else:
    print(','.join(ans))