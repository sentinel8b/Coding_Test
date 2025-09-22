n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid = [0]*(100+1)
for i in range(n):
    start_idx, end_idx = segments[i]
    for j in range(start_idx, end_idx+1):
        grid[j]+=1

print(max(grid))