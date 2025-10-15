A = input()
n = len(A)
cnt = 0
# Please write your code here.
for i in range(n-1):
    if A[i] == '(' and A[i+1] == '(':
        for j in range(i+2, n-1):
            if A[j] == ')' and A[j+1] == ')':
                cnt +=1
                
print(cnt)