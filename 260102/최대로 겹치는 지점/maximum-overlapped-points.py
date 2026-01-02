n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
tmp_list = [0 for _ in range(100)]

for (idx1, idx2) in segments:
    idx1 -= 1
    idx2 -= 1
    for i in range(idx1, idx2+1):
        tmp_list[i] += 1

best_val = 0
for i in tmp_list:
    if best_val < i:
        best_val = i
print(best_val)
