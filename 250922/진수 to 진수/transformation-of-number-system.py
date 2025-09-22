a, b = map(int, input().split())
n = input()

# Please write your code here.
i = 0
num_digit_10 = 0
for digit in reversed(n):
    digit = int(digit)
    cur_val = digit * a**i
    i += 1
    num_digit_10 += cur_val

digits = []
while True:
    if num_digit_10 < b:
        digits.append(num_digit_10)
        break
    digits.append(num_digit_10%b)
    num_digit_10//=b

for digit in digits[::-1]:
    print(digit, end = "")