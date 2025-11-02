from copy import deepcopy

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def cut_array(start_idx, end_idx):
    global n, blocks
    temp_arr = []

    for i in range(n):
        if i < start_idx or i > end_idx:
            temp_arr.append(blocks[i])
    
    n = len(temp_arr)
    for i in range(n):
        blocks[i] = temp_arr[i]

cut_array(s1-1, e1-1)
cut_array(s2-1, e2-1)

print(n)
for i in range(n):
    print(blocks[i])