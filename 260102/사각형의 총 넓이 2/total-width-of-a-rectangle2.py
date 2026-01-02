n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

sorted_x = sorted(x1+x2)[1:3]
sorted_y = sorted(y1+y2)[1:3]

print((x2[0] - x1[0]) * (y2[0] - y1[0]) + (x2[1] - x1[1]) * (y2[1] - y1[1]) - (sorted_x[1] - sorted_x[0]) * (sorted_y[1] - sorted_y[0]))