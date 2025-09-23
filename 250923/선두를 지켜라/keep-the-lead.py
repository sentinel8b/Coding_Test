n, m = map(int, input().split())



# Process A's movements
v = []
t = []
traj_A = [0]
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        last_pos = traj_A[-1]
        traj_A.append(last_pos + v)

# Process B's movements
v2 = []
t2 = []
traj_B = [0]
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        last_pos = traj_B[-1]
        traj_B.append(last_pos + v)

lead_status_list = []        
# Calculate who is leading 
for i in range(1, len(traj_A)):
    if traj_A[i] > traj_B[i]:
        lead_status_list.append(1)
    elif traj_B[i] > traj_A[i]:
        lead_status_list.append(0)

cnt = 0
for i in range(1,len(lead_status_list)):
    if i == 0 or lead_status_list[i] != lead_status_list[i-1]:
        cnt += 1

print(cnt)