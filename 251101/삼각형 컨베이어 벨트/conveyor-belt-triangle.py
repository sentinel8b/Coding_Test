n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))
d.reverse()


# Please write your code here.
for _ in range(t):
    l_r_temp = l[-1]
    r_d_temp = r[-1]
    d_l_temp = d[0]

    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = d_l_temp
    
    for i in range(n-1, 0, -1):
        r[i] = r[i-1]
    r[0] = l_r_temp

    for i in range(n-1):
        d[i] = d[i+1]
    d[-1] = r_d_temp

d.reverse()


for item in l:
    print(item, end = " ")
print()
for item in r:
    print(item, end = " ")
print()
for item in d:
    print(item, end = " ")