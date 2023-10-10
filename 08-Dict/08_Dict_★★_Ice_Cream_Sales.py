N = int(input())
dct = {}
for i in range(N):
    flavour,value = input().split()
    dct[flavour] = value

M = int(input())
cost = 0
dct_cost = {}
top_sales = []
buy_one = False
for i in range(M):
    key,amount = input().split()
    amount = float(amount)
    if key in dct:
        buy_one = True
        cost += int(dct[key])*amount
        if key in dct_cost:
            dct_cost[key] += int(dct[key])*amount
        else:
            dct_cost[key] = int(dct[key])*amount

temp_lst = []
for item in dct_cost:
    temp_lst.append([dct_cost[item],item])
temp_lst = sorted(temp_lst,reverse=True)

for i in range(len(temp_lst)):
    if temp_lst[i][0] == temp_lst[0][0]:
        top_sales.append(temp_lst[i][1])
top_sales = sorted(top_sales)
if buy_one == True:
    print("Total ice cream sales:",cost)
    print("Top sales:",end=" ")
    for i in range(len(top_sales)):
        if i == len(top_sales)-1:
            print(top_sales[i])
        else:
            print(top_sales[i],end=", ")
else:
    print("No ice cream sales")


