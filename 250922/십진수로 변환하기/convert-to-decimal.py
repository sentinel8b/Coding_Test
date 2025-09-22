binary = input()

# Please write your code here.
len_binary = len(binary)
i = 0
sum_digit_10 = 0
for digit in reversed(binary):
    cur_val = 2**i * int(digit)
    i += 1
    sum_digit_10 += cur_val

print(sum_digit_10)


