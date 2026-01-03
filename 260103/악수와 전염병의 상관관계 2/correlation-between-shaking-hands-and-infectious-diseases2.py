N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

tmp_list = [0 for _ in range(N+1)]
max_list = [0 for _ in range(N+1)]
sorted_hs = sorted(handshakes)
tmp_list[P] = 1

for i in range(len(sorted_hs)):
    f_man = sorted_hs[i][1]
    s_man = sorted_hs[i][2]
    if tmp_list[f_man] == 1 and tmp_list[s_man] != 1 and max_list[f_man] < K:
        tmp_list[s_man] = 1
        max_list[f_man] += 1
    elif tmp_list[s_man] == 1 and tmp_list[f_man] != 1 and max_list[s_man] < K:
        tmp_list[f_man] = 1
        max_list[s_man] += 1
    elif tmp_list[s_man] == 1 and tmp_list[f_man] == 1:
        max_list[f_man] += 1
        max_list[s_man] += 1

result = []
for i in tmp_list[1:]:
    result.append(str(i))
print(''.join(result))
