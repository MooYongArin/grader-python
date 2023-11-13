lst = []
def check(keyword):
    dct = {}
    lis = []
    for item in lst:
        dctUnique = {}
        unique = 0
        for subItem in item[1]:
            if subItem in dctUnique:
                dctUnique[subItem] += 1
            else:
                dctUnique[subItem] = 1
            if subItem == keyword:
                if item[0] in dct:
                    dct[item[0]] += 1
                else:
                    dct[item[0]] = 1
        for test in dctUnique:
            if dctUnique[test] == 1:
                unique += 1
        if unique == 0:
            unique = 1
        if item[0] in dct:
            lis.append([(dct[item[0]]/len(item[1]))*(1/unique),item[0]])
    lis.sort()
    if lis == []:
        return "NOT FOUND"
    else:
        return lis[-1][1]
for i in range(int(input())):
    fileName = input()
    inFile = input()
    lst.append([fileName,inFile.split()])
while True:
    find = input()
    if find == '-1':
        break
    print(check(find))