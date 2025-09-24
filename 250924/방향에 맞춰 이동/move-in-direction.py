n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# R L U D
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cur_x, cur_y = 0, 0

for i in range(n):
    move = dist[i]
    dir_str = dir[i]
    if dir_str == 'E':
        cur_x += move*dx[0]
        cur_y += move*dy[0]
    elif dir_str == 'W':
        cur_x += move*dx[1]
        cur_y += move*dy[1]
    elif dir_str == 'N':
        cur_x += move*dx[2]
        cur_y += move*dy[2]
    else: # D
        cur_x += move*dx[3]
        cur_y += move*dy[3]

print(cur_x, cur_y)