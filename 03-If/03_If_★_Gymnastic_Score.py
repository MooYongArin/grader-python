x = input().split()

temp_max = x[0]
temp_min = x[0]

for item in x:
    if item > temp_max:
        temp_max = item
    if item < temp_min:
        temp_min = item

x.remove(temp_max)
x.remove(temp_min)

x_avg = (float(x[0]) + float(x[1]))/2

print(round(x_avg,2))