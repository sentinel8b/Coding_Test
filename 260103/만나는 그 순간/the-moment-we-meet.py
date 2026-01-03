n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
tmp_list1 = [0]
tmp_list2 = [0]

for i in range(n):
    for j in range(t[i]):
        if d[i] == "R":
            tmp_list1.append(tmp_list1[-1] + 1)
        elif d[i] == "L":
            tmp_list1.append(tmp_list1[-1] - 1)

for i in range(m):
    for j in range(t2[i]):
        if d2[i] == "R":
            tmp_list2.append(tmp_list2[-1] + 1)
        elif d2[i] == "L":
            tmp_list2.append(tmp_list2[-1] - 1)

time = -1
if len(tmp_list1) == len(tmp_list2):
    for i in range(1, len(tmp_list1)):
        if tmp_list1[i] == tmp_list2[i]:
            time = i
            break

print(time)