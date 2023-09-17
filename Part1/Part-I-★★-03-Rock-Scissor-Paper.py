n = int(input())
p1_sc = 0
p2_sc = 0
for i in range(n*3):
    p1,p2 = input().split()

    if p1 != p2:
        if p1 == 'R' and p2 == 'S':
            p1_sc += 1
        elif p1 == 'R' and p2 == 'P':
            p2_sc += 1
        elif p1 == 'S' and p2 == 'P':
            p1_sc += 1
        elif p1 == 'S' and p2 == 'R':
            p2_sc += 1
        elif p1 == 'P' and p2 == 'R':
            p1_sc += 1
        elif p1 == 'P' and p2 == 'S':
            p2_sc += 1
    if p1_sc == n or p2_sc == n:
        break
    

print(p1_sc , p2_sc)
if p1_sc == n:
    print("Player 1 wins")
elif p2_sc == n:
    print("Player 2 wins")
else:
    print("Tie")
