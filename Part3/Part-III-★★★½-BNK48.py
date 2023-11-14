# สร้างพจนานุกรมเพื่อเก็บคะแนนโหวต
idol_scores = {}
idol_votes = {}
idol_kamioshi = {}
# รับข้อมูลนำเข้า
while True:
    try:
        line = input().strip()
        if line.isdigit():
            mode = int(line)
            break
        else:
            voter, idol, votes = line.split()
            votes = int(votes)
            # เพิ่มคะแนนโหวตให้แต่ละไอดอลตามโหวตแต่ละรอบ
            idol_scores[idol] = idol_scores.get(idol, 0) + votes
            # เพิ่มจำนวนโหวตให้แต่ละไอดอล
            idol_votes[idol] = idol_votes.get(idol, 0) + 1
            # เก็บจำนวนคามิโอชิของแต่ละไอดอล
            if voter == idol:
                idol_kamioshi[idol] = idol_kamioshi.get(idol, 0) + 1
    except EOFError:
        break
# จัดอันดับตามโหวตรวม
sorted_by_score = sorted(idol_scores.items(), key=lambda x: x[1], reverse=True)
top_by_score = [idol[0] for idol in sorted_by_score[:3]]

# จัดอันดับตามจำนวนโหวต
sorted_by_votes = sorted(idol_votes.items(), key=lambda x: x[1], reverse=True)
top_by_votes = [idol[0] for idol in sorted_by_votes[:3]]

# จัดอันดับตามจำนวนคามิโอชิ
sorted_by_kamioshi = sorted(idol_kamioshi.items(), key=lambda x: x[1], reverse=True)
top_by_kamioshi = [idol[0] for idol in sorted_by_kamioshi[:3]]

# ตรวจสอบโหมดและแสดงผลลัพธ์
if mode == 1:
    print(', '.join(top_by_score))
elif mode == 2:
    print(', '.join(top_by_votes))
elif mode == 3:
    print(', '.join(top_by_kamioshi))
