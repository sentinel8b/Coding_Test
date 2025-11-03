N, M, Q = map(int, input().split())


grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

def solve():

    global grid 

    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        r1z, c1z, r2z, c2z = r1 - 1, c1 - 1, r2 - 1, c2 - 1

        temp = grid[r1z][c1z]
        
        # 왼쪽 열 (아래 -> 위)
        for i in range(r1z, r2z):
            grid[i][c1z] = grid[i + 1][c1z]
            
        # 아래쪽 행 (오른쪽 -> 왼쪽)
        for j in range(c1z, c2z):
            grid[r2z][j] = grid[r2z][j + 1]
            
        # 오른쪽 열 (위 -> 아래)
        for i in range(r2z, r1z, -1):
            grid[i][c2z] = grid[i - 1][c2z]
            
        # 위쪽 행 (왼쪽 -> 오른쪽)
        for j in range(c2z, c1z + 1, -1):
            grid[r1z][j] = grid[r1z][j - 1]
            
        grid[r1z][c1z + 1] = temp


        temp_grid = [row[:] for row in grid]
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(r1z, r2z + 1):
            for j in range(c1z, c2z + 1):
                total_sum = grid[i][j]
                count = 1
                
                for k in range(4):
                    ni, nj = i + dr[k], j + dc[k]
                    
                    if 0 <= ni < N and 0 <= nj < M:
                        total_sum += grid[ni][nj]
                        count += 1
                
                temp_grid[i][j] = total_sum // count
        
        grid = temp_grid

# 함수 실행
solve()

# 최종 결과 출력
for row in grid:
    print(*row)