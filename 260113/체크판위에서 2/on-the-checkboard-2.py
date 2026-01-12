R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

color_list = ["B", "W"]

def find_idx(x, y, c):
    cand_idx = []
    next_color = c
    for i in range(x, R-1):
        for j in range(y, C-1):
            if grid[i+1][j+1] != c:
                cand_idx.append((i+1, j+1))
                next_color = grid[i+1][j+1]

    return cand_idx

cand_idx = find_idx(0, 0, grid[0][0])
nc = color_list[(color_list.index((grid[0][0])) + 1) % 2]
tmp_idx = []
for idx in cand_idx:
    tmp = find_idx(idx[0], idx[1], nc)
    for t in tmp:
        tmp_idx.append(t)

cand_idx = tmp_idx
nc = color_list[(color_list.index((nc)) + 1) % 2]
tmp_idx = []
for idx in cand_idx:
    tmp = find_idx(idx[0], idx[1], nc)
    for t in tmp:
        tmp_idx.append(t)

result = 0
for t in tmp_idx:
    if t == (R-1, C-1):
        result += 1

print(result)

