N = input()

# Please write your code here.
num_digit_10 = 0
i = 0

for digit in reversed(N):
    digit = int(digit)
    cur_val = digit * 2**i
    i += 1
    num_digit_10+=cur_val

target_val = num_digit_10*17

digits = []
while True:
    if target_val < 2:
        digits.append(target_val)
        break
    digits.append(target_val%2)
    target_val//=2

for digit in digits[::-1]:
    print(digit, end="")