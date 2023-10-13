def upgrade(x):
    if x == 'F':
        return 'D'
    elif x == 'D':
        return 'D+'
    elif x == 'D+':
        return 'C'
    elif x == 'C':
        return 'C+'
    elif x == 'C+':
        return 'B'
    elif x == 'B':
        return 'B+'
    elif x == 'B+':
        return 'A'
    else:
        return x


ids = []
grades = []
while True:
    x = input().split()
    if x == ['q']:
        break
    ids.append(x[0])
    grades.append(x[1])
uids = input().split()
for item in uids:
    if item in ids:
        for i in range(len(ids)):
            if ids[i] == item:
                grades[i] = upgrade(grades[i])
ans = []
for i in range(len(ids)):
    ans.append([ids[i],grades[i]])
ans.sort()
for item in ans:
    print(item[0],item[1])