n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

sorted_x = sorted(x)

result = 0
for i in range(len(sorted_x)):
    tmp_val = 0
    for j in range(sorted_x[i], sorted_x[i] + k + 1):
        if j in x:
            idx = x.index(j)
            if c[idx] == 'G':
                tmp_val += 1
            elif c[idx] == 'H':
                tmp_val += 2
    result = max(result, tmp_val)
print(result)