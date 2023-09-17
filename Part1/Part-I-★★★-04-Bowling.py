perform = input().strip()
frame_target = int(input())
sum_score = 0
frame_number = 0
mark = 0

for frame in range(1,11):
    if perform[frame_number:frame_number+3] == 'XXX':
        frame_n_score = 30
    elif perform[frame_number:frame_number+2] == 'XX':
        frame_n_score = 20 + int(perform[frame_number+2])
    elif perform[frame_number] == 'X' and perform[frame_number+2] == '/':
        frame_n_score = 20
    elif perform[frame_number] == 'X':
        frame_n_score = 10 + int(perform[frame_number+1]) + int(perform[frame_number+2])
    elif perform[frame_number+1:frame_number+3] == '/X':
        frame_n_score = 20
    elif perform[frame_number+1] == '/':
        frame_n_score = 10 + int(perform[frame_number+2])
    else:
        frame_n_score = int(perform[frame_number]) + int(perform[frame_number+1])
    sum_score += frame_n_score
    if perform[frame_number] == 'X':
        frame_number += 1
    else:
        frame_number += 2
    if frame == frame_target:
        print(frame_n_score)
        mark = 1
        break

if mark != 1:
    print(sum_score)