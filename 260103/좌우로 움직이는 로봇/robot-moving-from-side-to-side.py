n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
tmp_list1 = [0]
tmp_list2 = [0]

for i in range(n):
    for j in range(t[i]):
        if d[i] == "R":
            tmp_list1.append(tmp_list1[-1] + 1)
        else:
            tmp_list1.append(tmp_list1[-1] - 1)

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == "R":
            tmp_list2.append(tmp_list2[-1] + 1)
        else:
            tmp_list2.append(tmp_list2[-1] - 1)

result = 0
if len(tmp_list1) <= len(tmp_list2):
    for i in range(1, len(tmp_list2)):
        if i < len(tmp_list1):
            if tmp_list1[i] == tmp_list2[i] and tmp_list1[i-1] != tmp_list2[i-1]:
                result += 1
        else:
            if tmp_list1[-1] == tmp_list2[i] and tmp_list1[-1] != tmp_list2[i-1]:
                result += 1
else:
    for i in range(1, len(tmp_list1)):
        if i < len(tmp_list2):
            if tmp_list1[i] == tmp_list2[i] and tmp_list1[i-1] != tmp_list2[i-1]:
                result += 1
        else:
            if tmp_list1[i] == tmp_list2[-1] and tmp_list1[i-1] != tmp_list2[-1]:
                result += 1

print(result)