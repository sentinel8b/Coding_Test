N, T = map(int, input().split())
command_str = input()
board = [list(map(int, input().split())) for _ in range(N)]

def in_range(new_x, new_y):
    return new_x >= 0 and new_x < N and new_y >= 0 and new_y < N

# Please write your code here.
cur_x, cur_y = N//2 , N//2

dxs = [0, 1, 0, -1] # R D L U
dys = [1, 0, -1, 0]

dir_idx = 3
to_be_summed = [board[cur_x][cur_y]]

for cmd in command_str:
    if cmd == 'R':
        dir_idx = (dir_idx + 1)%4
    elif cmd == 'L':
        dir_idx = (dir_idx -1 + 4)%4
    else: # F 
        new_x = cur_x + dxs[dir_idx]
        new_y = cur_y + dys[dir_idx]
        if in_range(new_x, new_y):
            cur_x = new_x
            cur_y = new_y
            to_be_summed.append(board[cur_x][cur_y])

print(sum(to_be_summed))

