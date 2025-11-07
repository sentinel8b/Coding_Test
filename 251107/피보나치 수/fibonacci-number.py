n = int(input())

memory = [0] * 46

memory[1] = 1
memory[2] = 1

def fibo(n):
    if n <= 2:
        return memory[n]

    else:
        return fibo(n-1) + fibo(n-2)

ans = fibo(n)

print(ans)