dct = {}
lst = []
N = int(input())
for i in range(N):
    _id,location = [x.strip() for x in input().split(':')]
    location = set([x.strip() for x in location.split(',')])
    dct[_id] = location
    lst.append(_id)
find = input().strip()
check = False
for item in lst:
    if item != find and len(dct[item] & dct[find]) > 0:
        print(item)
        check = True
if not check:
    print("Not Found")