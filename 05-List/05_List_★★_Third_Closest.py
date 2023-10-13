n = int(input())

lst = []
for i in range(1,n+1):
    x,y = [float(e) for e in input().split()]
    distance = ((x)**2 + (y)**2)**0.5
    index = i
    lst.append([distance,i,x,y])

lst.sort()
print('#' + str(lst[2][1]) + ':' ,(lst[2][2],lst[2][3]))