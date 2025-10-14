import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
min_value = sys.maxsize
# iterating over starting point
for i in range(n):
    dist = 0
    assign_list = a.copy()
    new_assign_list = assign_list[i+1:] + assign_list[:i]
    for j in range(len(new_assign_list)):
        dist += (j+1)*new_assign_list[j]

    min_value = min(min_value, dist)

print(min_value)

    