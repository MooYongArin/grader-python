_file,year = input().split()
main_file = open(_file)
all_text = main_file.read().split()

lst_number = []
lst_score = []
for item in all_text:
    if len(item) == 10:
        lst_number.append(item)
    else:
        lst_score.append(item)
_sum = 0
count = 0
_min = 100
_max = 0
check = False
for i in range(len(lst_number)):
    if lst_number[i][:2] == year[2:]:
        check = True
        count += 1
        _sum += float(lst_score[i])
        if float(lst_score[i]) <= _min:
            _min = float(lst_score[i])
        if float(lst_score[i]) >= _max:
            _max = float(lst_score[i])
if check:
    print(_min,_max,_sum/count)
else:
    print("No data")
