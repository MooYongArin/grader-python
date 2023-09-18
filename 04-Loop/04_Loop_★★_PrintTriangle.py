n = int(input())

print("."*(n-1)+"*")

for i in range(n-1,1,-1):
    j = n-i
    print("."*(i-1)+"*"+"."*(2*j-1)+"*")

print("*"*(2*n-1))