n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
picked_lines = []

def find_max_lines(curr_idx):
    global max_cnt

    if curr_idx == n:
        max_cnt = max(max_cnt, len(picked_lines))
        return

    find_max_lines(curr_idx + 1)
    new_line = lines[curr_idx]
    l1, r1 = new_line

    is_compatible = True
    for picked_line in picked_lines:
        l2, r2 = picked_line
        if r1 >= l2 and r2 >= l1:
            is_compatible = False
            break

    if is_compatible:
        picked_lines.append(new_line)
        find_max_lines(curr_idx+1)
        picked_lines.pop()

find_max_lines(0)
print(max_cnt)