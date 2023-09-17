y = [int(x) for x in input().split()]
count = 0
for i in range(1,len(y)-1):
  if y[i] > y[i-1] and y[i] > y[i+1]:
    count += 1
print(count)