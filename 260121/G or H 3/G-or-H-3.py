n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
result = 0
for i in range(max(x) - k):
    tmp_val = 0
    for j in range(i+1, i+1+k+1):
        if j in x:
            idx = x.index(j)
            if c[idx] == 'G':
                tmp_val += 1
            elif c[idx] == 'H':
                tmp_val += 2
    result = max(result, tmp_val)
print(result)