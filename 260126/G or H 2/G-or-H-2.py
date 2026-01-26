n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
# pos_list = [0 for _ in range(101)]
# for i in range(len(pos)):
#     p = pos[i]
#     pos_list[p] = alpha[i]

sorted_pos = sorted(pos)
sorted_alpha = []
sorted_idx = []
for i in range(len(sorted_pos)):
    sorted_alpha.append(alpha[pos.index(sorted_pos[i])])
    sorted_idx.append(sorted_pos[i])

min_idx, max_idx = sorted_pos[0], sorted_pos[-1]
max_val = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        G_cnt = 0
        H_cnt = 0
        for a in sorted_alpha[i:j]:
            if a == 'G':
                G_cnt += 1
            elif a == 'H':
                H_cnt += 1
        
        if G_cnt == H_cnt:
            max_val = max(max_val, sorted_idx[j-1] - sorted_idx[i])
print(max_val)