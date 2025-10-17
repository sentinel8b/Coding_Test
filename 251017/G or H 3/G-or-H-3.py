n, k = map(int, input().split())
x = []
c = []
max_pos = 10000
arr = [0] * (max_pos+1)
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
    if char == 'G':
        arr[int(pos)] = 1
    else:
        arr[int(pos)] = 2

max_val = 0
k_adjusted = k+1
# Please write your code here.
for i in range(len(arr)-k_adjusted + 1):
    max_val = max(max_val, sum(arr[i:i+k_adjusted]))

print(max_val)
