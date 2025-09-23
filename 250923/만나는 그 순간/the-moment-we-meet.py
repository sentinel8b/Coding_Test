n, m = map(int, input().split())

d = []
t = []

d2 = []
t2 = []

for i in range(n):
    dir_str, time = input().split()
    time = int(time)
    d.append(dir_str)
    t.append(time)

for i in range(m):
    dir_str, time = input().split()
    time = int(time)
    d2.append(dir_str)
    t2.append(time)

# Please write your code here.
traj_list = [0]
traj_list2 = [0]

for dir_str, time in zip(d, t):
    last_pos = traj_list[-1]
    if dir_str == 'R':
        for i in range(1,time+1):
            traj_list.append(last_pos+i)
    else: # L
        for i in range(1,time+1):
            traj_list.append(last_pos-i)

for dir_str, time in zip(d2, t2):
    last_pos = traj_list2[-1]
    if dir_str == 'R':
        for i in range(1,time+1):
            traj_list2.append(last_pos+i)
    else: # L
        for i in range(1,time+1):
            traj_list2.append(last_pos-i)

for i in range(1,min(len(traj_list), len(traj_list2))):
    if traj_list[i] == traj_list2[i]:
        print(i)
        break
else:
    print(-1)     