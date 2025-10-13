n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def calc_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
min_value = 10000000
# Please write your code here.
for i in range(1,n-1):
    copy_x = x.copy()
    copy_y = y.copy()
    copy_x.pop(i)
    copy_y.pop(i)
    dist = 0
    for j in range(len(copy_x)-1):
        dist += calc_distance(copy_x[j], copy_y[j], copy_x[j+1], copy_y[j+1])
    min_value = min(dist, min_value)
print(min_value)
