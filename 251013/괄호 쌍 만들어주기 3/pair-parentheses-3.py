A = input()

# Please write your code here.
num_len = len(A)

cnt = 0

for i in range(num_len):
    if A[i] == '(':
        for j in range(i+1, num_len):
            if A[j] == ')':
                cnt +=1

print(cnt)