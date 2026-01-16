A = input()

# Please write your code here.
idx = 0
for i in range(len(A)-1):
    if A[i:i+2] == "((":
       for j in range(i+1, len(A)-1):
        if A[j:j+2] == "))":
            idx += 1
print(idx) 