A = input()

# Please write your code here.
result = 0

for i in range(len(A)):
    a = A[i]
    if a == "(":
        for j in range(i, len(A)):
            b = A[j]
            if b == ")":
                result += 1
print(result)

