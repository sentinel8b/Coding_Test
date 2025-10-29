n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
picked_lines = [] # lines will be added

def is_valid(line_list):
    if len(line_list) > 1:
        pivot = line_list[-1] # 가장 최근에 뽑은 선
        pivot_start = pivot[0]
        pivot_end = pivot[1]
        for line in line_list[:-1]: # 자기 빼고 이전 선 순회하면서
            line_start = line[0]
            line_end = line[1]
            if line_start <= pivot_start <= line_end or line_start <= pivot_end <= line_end:
                return False
        return True
    else:
        return True


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