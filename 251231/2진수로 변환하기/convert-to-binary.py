n = int(input())

# Please write your code here.
dig = 0
n_dig = n
i = 0
while True:
    dig += 10**i * (n % 2)
    n = n // 2
    i += 1

    if n == 1:
        dig += 10**i * (n % 2)
        break
    elif n == 0:
        dig *= 10
        break
    

print(dig)