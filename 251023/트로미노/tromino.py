n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x>=0 and x < n and y>=0 and y<m

def calc_max_block_sum(x, y):
    max_sum = 0
    
    if in_range(x, y + 2):
        current_sum = grid[x][y] + grid[x][y+1] + grid[x][y+2]
        max_sum = max(max_sum, current_sum)

    if in_range(x + 2, y): 
        current_sum = grid[x][y] + grid[x+1][y] + grid[x+2][y]
        max_sum = max(max_sum, current_sum)
        
    if in_range(x + 1, y + 1): 
        # (x,y), (x,y+1), (x+1,y), (x+1,y+1)
        s1 = grid[x][y] + grid[x][y+1] + grid[x+1][y]     
        s2 = grid[x][y] + grid[x][y+1] + grid[x+1][y+1] 
        s3 = grid[x][y] + grid[x+1][y] + grid[x+1][y+1] 
        s4 = grid[x][y+1] + grid[x+1][y] + grid[x+1][y+1] 
        
        max_sum = max(max_sum, s1, s2, s3, s4)

    return max_sum

ans = 0

for x in range(n):
    for y in range(m):
        block_sum = calc_max_block_sum(x, y)
        ans = max(ans, block_sum) 

print(ans)