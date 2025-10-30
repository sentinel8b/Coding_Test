import sys
n = int(input())
jump_list = list(map(int,input().split()))

min_cnt = sys.maxsize
flag = False

def move(cnt, curr_pos):
    global min_cnt
    global flag

    if curr_pos == n:
        min_cnt = min(min_cnt, cnt)

    if curr_pos == n:
        min_cnt = min(min_cnt, cnt)
        flag = True
        return

    curr_val = jump_list[curr_pos-1]
    for dx in range(1, curr_val+1):
        if curr_pos + dx > n:
            continue
        move(cnt + 1, curr_pos + dx)

move(0, 1)

if not flag:
    print(-1)
else:
    print(min_cnt)
