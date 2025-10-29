n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
picked_lines = [] # lines will be added

def is_valid(line_list):
    valid_flag = True

    #empty or has only one element
    if len(line_list) <= 1:
        return True

    line_list = sorted(line_list, key = lambda x : x[0]) # sort based on starting pt
    for i in range(1, len(line_list)):
        line1_end = line_list[i-1][1]
        line2_start = line_list[i][0]
        if line2_start > line1_end:
            continue
        else:
            valid_flag = False
    return valid_flag

def pick_lines():
    global picked_lines
    global max_cnt
    if is_valid(picked_lines):
        max_cnt = max(max_cnt, len(picked_lines))
        for item in lines:
            picked_lines.append(item)
            pick_lines()
    else:
        picked_lines.pop()
        return

pick_lines()

print(max_cnt)