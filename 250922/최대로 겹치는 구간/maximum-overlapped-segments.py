n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid = [0]*200

for i in range(n):
    start_idx, end_idx = segments[i]
    start_idx+=100
    end_idx+=100
    for j in range(start_idx, end_idx):
        grid[j]+=1

print(max(grid))