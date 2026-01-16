n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(x, y, ref_x, ref_y):
    return x > ref_x or y > ref_y
max_val = 0
for i in range(n):
    for j in range(n-2):
        sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        for k in range(i, n):
            for w in range(n-2):
                if in_range(w, k, j+2, i):
                    sum2 = arr[k][w] + arr[k][w+1] + arr[k][w+2]
                    max_val = max(max_val, sum1+sum2)
print(max_val)
