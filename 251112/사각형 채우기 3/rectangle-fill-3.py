N = int(input())
MOD = 1_000_000_007


f = [0] * max(N + 1, 3)
h = [0] * max(N + 1, 3)

# N=0 일 때
f[0] = 1  
h[0] = 0

# N=1 일 때
f[1] = 2  # (2x1 세로 1개) 또는 (1x1 가로 2개)
h[1] = 1  # (아래쪽 1x1 1개, 위는 비움)


for i in range(2, N + 1):
    f[i] = (2 * f[i-1] + f[i-2] + 2 * h[i-1]) % MOD

    h[i] = (f[i-1] + h[i-1]) % MOD

print(f[N])