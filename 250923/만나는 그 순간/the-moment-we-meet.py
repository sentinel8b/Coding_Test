# n, m = map(int, input().split())

# d = []
# t = []

# d2 = []
# t2 = []

# for i in range(n):
#     dir_str, time = input().split()
#     time = int(time)
#     d.append(dir_str)
#     t.append(time)

# for i in range(m):
#     dir_str, time = input().split()
#     time = int(time)
#     d2.append(dir_str)
#     t2.append(time)

# # Please write your code here.
# traj_list = [0]
# traj_list2 = [0]

# for dir_str, time in zip(d, t):
#     last_pos = traj_list[-1]
#     if dir_str == 'R':
#         for i in range(1,time+1):
#             traj_list.append(last_pos+i)
#     else: # L
#         for i in range(1,time+1):
#             traj_list.append(last_pos-i)

# for dir_str, time in zip(d2, t2):
#     last_pos = traj_list2[-1]
#     if dir_str == 'R':
#         for i in range(1,time+1):
#             traj_list2.append(last_pos+i)
#     else: # L
#         for i in range(1,time+1):
#             traj_list2.append(last_pos-i)

# for i in range(1,min(len(traj_list), len(traj_list2))):
#     if traj_list[i] == traj_list2[i]:
#         print(i)
#         break
# else:
#     print(-1)     

MAX_T = 1000000

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        print(i)
        break
else:
    print(-1)