n = int(input())
arr = [int(input()) for _ in range(n)]

max_val = 0

def check_carry_three(num1, num2, num3):
    while num1 > 0 or num2 > 0 or num3 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        digit3 = num3 % 10
        
        if digit1 + digit2 + digit3 >= 10:
            return True  
            
        num1 //= 10
        num2 //= 10
        num3 //= 10
        
    return False

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num1, num2, num3 = arr[i], arr[j], arr[k]
            if not check_carry_three(num1, num2, num3):
                max_val = max(num1+num2+num3, max_val)

if max_val == 0:
    print(-1)
else:
    print(max_val)