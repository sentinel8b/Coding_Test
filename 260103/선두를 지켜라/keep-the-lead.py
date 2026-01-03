n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

tmp_list1 = [0]
tmp_list2 = [0]

for i in range(n):
    for j in range(t[i]):
        tmp_list1.append(tmp_list1[-1] + v[i])

for i in range(m):
    for j in range(t2[i]):
        tmp_list2.append(tmp_list2[-1] + v2[i])

result = 0
front = 0
for i in range(1, len(tmp_list1)):
    if tmp_list1[i] > tmp_list2[i]:
        if front != 1:
            result += 1
        front = 1
    elif tmp_list1[i] < tmp_list2[i]:
        if front != 2:
            result += 1
        front = 2
    
print(result-1)