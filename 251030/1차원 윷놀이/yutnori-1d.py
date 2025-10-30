n, m, k = map(int, input().split())
move_list = list(map(int, input().split()))

max_score = 0
target_idx = m-1

pos_per_unit = [1] * (k+1)

def calc_score():
    score = 0
    for i in range(len(pos_per_unit)):
        if pos_per_unit[i] >= m:
            score += 1
    return score

def make_move(turn):
    global max_score 
    global move_list
    if turn == n:
        case_score = calc_score()  
        max_score = max(max_score, case_score)    
        return  

    for i in range(1,k+1):
        if pos_per_unit[i] < m:
            pos_per_unit[i] += move_list[turn]
            make_move(turn+1)
            pos_per_unit[i] -= move_list[turn]
        else:
            continue

make_move(0)
print(max_score)