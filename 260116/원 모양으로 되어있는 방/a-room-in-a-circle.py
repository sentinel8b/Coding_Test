n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
def count_dist(a_list):
    dist = 0
    for i in range(len(a_list)):
        dist += (a_list[i] * i)
    return dist
min_dist = sys.maxsize
for i in range(n):
    tmp_a = a[i:] + a[:i]
    min_dist = min(min_dist, count_dist(tmp_a))
print(min_dist)