n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def check_carry(a, b, c):
    max_size = max(len(a), len(b))
    max_size = max(max_size, len(c))
    a = [0 for _ in range(max_size - len(a))] + a
    b = [0 for _ in range(max_size - len(b))] + b
    c = [0 for _ in range(max_size - len(c))] + c

    for i in range(max_size):
        sum = int(a[::-1][i]) + int(b[::-1][i]) + int(c[::-1][i])
        if sum >= 10:
            return True
    return False

result = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if not check_carry(list(str(arr[i])), list(str(arr[j])), list(str(arr[k]))):
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)