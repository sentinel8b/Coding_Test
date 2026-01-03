N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]
dir_dict = {'W':0,'S':1,'N':2,'E':3}

init_loc = [0,0]
init_time = -1
time_count = 0

for n in range(N):
    for d in range(dist[n]):
        time_count += 1
        init_loc[0] += dx[dir_dict[dir[n]]]
        init_loc[1] += dy[dir_dict[dir[n]]]
        if init_loc[0] == 0 and init_loc[1] == 0:
            init_time = time_count
            break
print(init_time)