perform = input().strip()
frame_target = int(input())
sum_score = 0
frame_number = 0
frame_n_score = int()

for item in perform:
    if item == 'X':
        frame_number += 1
    elif item == '/':
        frame_number += 1
    


for frame in range(1,11):

    if perform[frame] == 'X' and perform[frame+1] == 'X' and perform[frame+2] == 'X' :
        frame_n_score = 30
    elif perform[frame] == 'X' and perform[frame+1] == 'X' and (perform[frame+2] != '/' or perform[frame+2] != 'X'):
        frame_n_score = 20 + int(perform[frame+2])
    elif perform[frame] == 'X' and (perform[frame+1] != '/' or perform[frame+1] != 'X') and perform[frame+2] == '/':
        frame_n_score = 20
    elif perform[frame] == 'X' and (perform[frame+1] != '/' or perform[frame+1] != 'X') and (perform[frame+2] != '/' or perform[frame+2] != 'X'):
        frame_n_score = 10 + int(perform[frame+1]) + int(perform[frame+2])
    elif (perform[frame] != '/' or perform[frame] != 'X') and perform[frame+1] != '/' and perform[frame+2] == 'X':
        frame_n_score = 20
    elif (perform[frame] != '/' or perform[frame] != 'X') and perform[frame+1] != '/' and (perform[frame+2] != '/' or perform[frame+2] != 'X'):
        frame_n_score = 10 + int(perform[frame+2])
    elif (perform[frame] != '/' or perform[frame] != 'X') and (perform[frame+1] != '/' or perform[frame+1] != 'X'):
        frame_n_score = int(perform[frame]) + int(perform[frame+1])

    print(frame_n_score)
    sum_score += frame_n_score
    if frame == frame_target:
        print(frame_n_score)
        mark = 1

if mark != 1:
    print(sum_score)