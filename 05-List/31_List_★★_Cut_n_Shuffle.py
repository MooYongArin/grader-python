count_card = 0
card = input().split()
saved_cards = []
cutNshuffle = input()

for x in card:
    saved_cards.append(x)
    count_card = count_card + 1

for method in cutNshuffle:
    if method == "C":
        # Cut
        for i in range(0,count_card):
            if i < int(0.5*count_card):
                card[i] = saved_cards[i+int(0.5*count_card)]
            elif i >= int(0.5*count_card):
                card[i] = saved_cards[i-int(0.5*count_card)]
        saved_cards = []
        for x in card:
            saved_cards.append(x)
    elif method == "S":
        # Shuffle
        for i in range(0,count_card):
            if i < int(0.5*count_card):
                card[2*i] = saved_cards[i]
                card[(2*i)+1] = saved_cards[i+int(0.5*count_card)]
        saved_cards = []
        for x in card:
            saved_cards.append(x)

print(' '.join(card))