n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys
def manh_dist(x1,y1,x2,y2):
    return int(((x1 - x2) ** 2) ** 0.5 + ((y1 - y2) ** 2) ** 0.5)

min_dist = sys.maxsize
start_x, start_y = x[0], y[0]
for i in range(n-2):
    x_tmp = x[:i+1] + x[i+2:]
    y_tmp = y[:i+1] + y[i+2:]
    start_x, start_y = x_tmp[0], y_tmp[0]
    dist = 0
    for j in range(n-2):
        dist += manh_dist(start_x, start_y, x_tmp[j+1], y_tmp[j+1])
        start_x, start_y = x_tmp[j+1], y_tmp[j+1]
    min_dist = min(min_dist, dist)
print(min_dist)