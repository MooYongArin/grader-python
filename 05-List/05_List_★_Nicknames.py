lst = [['Robert','Dick'],['William','Bill'],['James','Jim'],['John','Jack'],['Margaret','Peggy'],['Edward','Ed'],['Sarah','Sally'],['Andrew','Andy'],['Anthony','Tony'],['Deborah','Debbie']]
real_name = []
ans = []
n = int(input())
for i in range(n):
    x = input()
    real_name.append(x)

for item in real_name:
    mark = 0
    for i in range(10):
        if item == lst[i][0]:
            ans.append(lst[i][1])
            mark = 1
        elif item == lst[i][1]:
            ans.append(lst[i][0])
            mark = 1
    if mark == 0:
        ans.append('Not found')

for item in ans:
    print(item)