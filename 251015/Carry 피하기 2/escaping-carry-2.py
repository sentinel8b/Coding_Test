n = int(input())
arr = [int(input()) for _ in range(n)]

max_val = 0

def _check_carry_pair(num1, num2):
    while num1 > 0 and num2 > 0:
        digit_num1 = num1%10
        digit_num2 = num2%10
        if digit_num1 + digit_num2 >= 10:
            return True
        num1 = num1//10
        num2 = num2//10
    return False

# Please write your code here.
def check_carry(num1, num2, num3):
    return _check_carry_pair(num1, num2) or _check_carry_pair(num1, num3) or _check_carry_pair(num2, num3)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num1, num2, num3 = arr[i], arr[j], arr[k]
            if not check_carry(num1, num2, num3):
                max_val = max(num1+num2+num3, max_val)

if max_val == 0:
    print(-1)
else:
    print(max_val)