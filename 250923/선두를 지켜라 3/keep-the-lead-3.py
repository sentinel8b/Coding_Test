N, M = map(int, input().split())

# Process A's movements
traj_A = [0]
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        last_val = traj_A[-1]
        traj_A.append(last_val + v)

# Process B's movements
traj_B = [0]
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        last_val = traj_B[-1]
        traj_B.append(last_val + v)

hof_per_time = []

for i in range(0, len(traj_A)):
    if traj_A[i] > traj_B[i]:
        hof_per_time.append(1)
    elif traj_B[i] > traj_A[i]:
        hof_per_time.append(0)
    else: # ==
        hof_per_time.append(2)

cnt = 0
for i in range(1, len(hof_per_time)):
    if hof_per_time[i] != hof_per_time[i-1]:
        cnt += 1

print(cnt)

