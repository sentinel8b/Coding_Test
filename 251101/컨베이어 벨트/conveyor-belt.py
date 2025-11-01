n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
d.reverse()



# Please write your code here.
for _ in range(t):
    d_u_temp = d[0]
    u_d_temp = u[-1]

    # push d (R -> L)
    for i in range(n-1):
        d[i] = d[i+1]
    d[-1] = u_d_temp

    # push u (L -> R)
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
    u[0] = d_u_temp

d.reverse()

for item in u:
    print(item, end = " ")
print()
for item in d:
    print(item, end = " ")
