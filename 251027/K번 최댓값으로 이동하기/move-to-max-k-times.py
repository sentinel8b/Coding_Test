from collections import deque
import sys

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

x, y = r-1, c-1

# U R D L
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(nx, ny, start_val, visited):
    if not in_range(nx, ny):
        return False
    if visited[nx][ny] or grid[nx][ny] >= start_val:
        return False
    return True

def need_update(best_pos, new_pos):
    if best_pos == (-1, -1):
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    if (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y):
        return True
    
    return False

for _ in range(k):
    visited = [[0] * n for _ in range(n)]
    bfs_q = deque()
    
    best_pos = (-1, -1) 
    

    start_val = grid[x][y] 
    bfs_q.append((x, y))
    visited[x][y] = 1 
    
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = curr_x + dx
            ny = curr_y + dy
            
            if can_go(nx, ny, start_val, visited):
                visited[nx][ny] = 1
                bfs_q.append((nx, ny))

                new_pos = (nx, ny)
                if need_update(best_pos, new_pos):
                    best_pos = new_pos
                    
    if best_pos == (-1, -1):
        break
    else:
        x, y = best_pos

print(x+1, y+1)
