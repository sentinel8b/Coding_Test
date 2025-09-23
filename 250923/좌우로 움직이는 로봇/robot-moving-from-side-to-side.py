n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
traj_A = [0]
for _ in range(n):
    time, direction = input().split()
    for i in range(int(time)):
        last_val = traj_A[-1]
        traj_A.append(last_val + 1 if direction == 'R' else last_val - 1)

# Process robot B's movements
t_b = []
d_b = []
traj_B = [0]
for _ in range(m):
    time, direction = input().split()
    for i in range(int(time)):
        last_val = traj_B[-1]
        traj_B.append(last_val + 1 if direction == 'R' else last_val -1)

# pad the empty timestep of short case
len_traj_A = len(traj_A)
len_traj_B = len(traj_B)

if len_traj_A < len_traj_B:
    for _ in range(len_traj_B - len_traj_A):
        traj_A.append(traj_A[-1])
else:
    for _ in range(len_traj_A - len_traj_B):
        traj_B.append(traj_B[-1])

# Trace the matching cases
cnt = 0
for i in range(1, len(traj_A)):
    if traj_A[i] == traj_B[i]:
        if traj_A[i-1] != traj_B[i-1]:
            cnt += 1

print(cnt)