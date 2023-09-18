x = input().split()
x.sort()
unique_num = []
unique_num_ten = []
unique_num_count = 0

for num in x:
    if num not in unique_num:
        unique_num_count = unique_num_count + 1
        unique_num.append(num)

unique_num.sort(key=int)
for i in range(10):
    unique_num_ten.append(unique_num[i])

unique_num_ten.sort(key=int)
print(unique_num_count)
unique_num_ten_no_quotes = '[' + ', '.join(unique_num_ten) + ']'
print(unique_num_ten_no_quotes)
