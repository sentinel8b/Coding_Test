n = int(input())
S = input()

# Please write your code here.
idx = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if S[i] == 'C' and S[j] == 'O' and S[k] == 'W':
                idx += 1
print(idx)