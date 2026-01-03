n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dir_dict = {'E' : 0, 'S' : 1, 'W' : 2, 'N' : 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

result_x, result_y = 0, 0
for i in range(n):
    result_x += dx[dir_dict[dir[i]]] * dist[i]
    result_y += dy[dir_dict[dir[i]]] * dist[i]
print(result_x,result_y)
