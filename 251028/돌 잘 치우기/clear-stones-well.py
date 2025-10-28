import itertools
from copy import deepcopy
from collections import deque

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pts = [list(map(int, input().split())) for _ in range(k)]

def in_range(x, y):
    return 0<= x < n and 0<= y <n

# def can_go(x,y,grid,visited):
#     if not in_range(x,y):
#         return False
#     if visited[x][y]:
#         return False
#     if grid[x][y] == 1:
#         return False
#     return True

# def bfs(x, y):
#     # U R D L
#     dxs = [-1, 0, 1, 0]
#     dys = [0, 1, 0, -1]

#     global global_visited
#     global temp_grid
#     visited = [[0] * n for _ in range(n)]
#     bfs_q = deque([(x, y)])
#     visited[x][y] = 1
#     global_visited[x][y] = 1
#     while bfs_q:
#         x, y = bfs_q.popleft()
#         for dx, dy in zip(dxs, dys):
#             nx = x + dx
#             ny = y + dy
#             if can_go(nx, ny, temp_grid, visited):
#                 visited[nx][ny] = 1
#                 global_visited[nx][ny] = 1
#                 bfs_q.append((nx, ny))
    
def bfs(start_points, grid_for_bfs, visited_for_bfs):
    # U R D L
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    # 1. 큐(deque)를 비어있는 상태로 생성
    bfs_q = deque()

    # 2. K개의 모든 시작점을 큐에 추가하고 방문 처리
    for point in start_points:
        # (주의: 문제 입력은 1-based, 우리는 0-based 사용)
        x, y = point[0] - 1, point[1] - 1
        
        # 시작점이 돌(1)이 아니거나, 이미 방문한 곳이 아닐 때만 큐에 추가
        # (시작점이 돌 위에 있을 수도 있으니 확인)
        if grid_for_bfs[x][y] == 0 and not visited_for_bfs[x][y]:
            bfs_q.append((x, y))
            visited_for_bfs[x][y] = 1 # ⭐️ global_visited를 직접 수정

    # 3. BFS 실행 (이 부분은 거의 동일)
    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            # can_go는 visited_for_bfs를 사용하도록 수정 필요
            if can_go(nx, ny, grid_for_bfs, visited_for_bfs): 
                visited_for_bfs[nx][ny] = 1 # ⭐️ global_visited를 직접 수정
                bfs_q.append((nx, ny))

# -------------------------------------------------
# 💡 can_go 함수도 파라미터에 맞게 수정
# -------------------------------------------------
def can_go(x, y, grid, visited): # 이제 global 변수를 안 써요
    if not in_range(x, y):
        return False
    if visited[x][y]: # 
        return False
    if grid[x][y] == 1:
        return False
    return True

def get_stone_coord_list(grid):
    coord_list = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                coord_list.append((x,y))
    return coord_list


# stone_coord_list = get_stone_coord_list(grid)
# stone_combs = itertools.combinations(stone_coord_list, m)

# max_val = 0

# for comb in stone_combs:
#     temp_grid = deepcopy(grid)
#     global_visited = [[0] * n for _ in range(n)]
#     case_val = 0

#     for stone_coord in comb:
#         stone_x, stone_y = stone_coord
#         temp_grid[stone_x][stone_y] = 0
        
#     for start_coord in pts:
#         start_x, start_y = start_coord
#         start_x -= 1
#         start_y -= 1
#         bfs(start_x, start_y)

#     for x in range(n):
#         for y in range(n):
#             if global_visited[x][y] == 1:
#                 case_val += 1
#     max_val = max(case_val, max_val)

# print(max_val)

stone_coord_list = get_stone_coord_list(grid)
stone_combs = itertools.combinations(stone_coord_list, m)

max_val = 0

for comb in stone_combs:
    # 1. ⭐️ 깊은 복사 (Deep Copy) 사용
    temp_grid = deepcopy(grid) 
    global_visited = [[0] * n for _ in range(n)] # 방문 기록 초기화
    case_val = 0

    # 2. 돌 제거 (이 부분은 동일)
    for stone_coord in comb:
        stone_x, stone_y = stone_coord
        temp_grid[stone_x][stone_y] = 0

    # 3. ⭐️ K번 반복하던 루프가 사라지고, 단 한 번 호출!
    #    시작점 리스트(pts), 복사된 맵, 방문 기록 배열을 넘겨줍니다.
    bfs(pts, temp_grid, global_visited)

    # 4. 결과 계산 (이 부분은 동일)
    for x in range(n):
        for y in range(n):
            if global_visited[x][y] == 1:
                case_val += 1
    max_val = max(case_val, max_val)

print(max_val)