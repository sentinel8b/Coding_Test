n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_val = 0
# Please write your code here.
for i in range(n):
    for j in range(n):
    # two grid per one row
        grid1_max = 0
        grid2_max = 0
        if i == j:
            if n >= 6:
                for grid1_center in range(1, n-1): # select center of grid
                    for grid2_center in range(grid1_center+3, n-1):
                        grid1_sum = arr[i][grid1_center-1] + arr[i][grid1_center] + arr[i][grid1_center+1]
                        grid2_sum = arr[i][grid2_center-1] + arr[i][grid2_center] + arr[i][grid2_center+1]
                        max_val = max(grid1_sum + grid2_sum, max_val)
        else:
            for grid1_center in range(1, n-1):
                grid1_sum = arr[i][grid1_center-1] + arr[i][grid1_center] + arr[i][grid1_center+1]
                grid1_max = max(grid1_max, grid1_sum)
            for grid2_center in range(1, n-1):
                grid2_sum = arr[j][grid2_center-1] + arr[j][grid2_center] + arr[j][grid2_center+1]
                grid2_max = max(grid2_max, grid2_sum)

            max_val = max(grid1_max + grid2_max, max_val)

print(max_val)

                
