N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

tmp_list1 = [0]
tmp_list2 = [0]

best_list = [0]

for n in range(N):
    for i in range(t[n]):
        tmp_list1.append(tmp_list1[-1] + v[n])

for m in range(M):
    for i in range(t2[m]):
        tmp_list2.append(tmp_list2[-1] + v2[m])

for i in range(1, len(tmp_list1)):
    if tmp_list1[i] > tmp_list2[i] and best_list[-1] != 'A':
        best_list.append('A')
    elif tmp_list1[i] < tmp_list2[i] and best_list[-1] != 'B':
        best_list.append('B')
    elif tmp_list1[i] == tmp_list2[i] and best_list[-1] != 'AB':
        best_list.append('AB')

print(len(best_list) - 1)