count_card = 0
card = input().split()
cutNshuffle = input()

for x in card:
    count_card = count_card + 1

for i in range(1,count_card):
    card[i-1] = card[count_card-i]

print(card)