def grade_mcq(sol, ans):
    score = 0
    if len(sol) == len(ans):
        for i in range(len(ans)):
            if sol[i] == ans[i]:
                score = score + 1
        return score
    else:
        return -1

exec(input())