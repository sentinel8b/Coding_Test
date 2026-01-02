a, b = map(int, input().split())
n = input()

# Please write your code here.
t = 0
for i in range(len(n)):
    t += a ** i * int(n[::-1][i])

tmp_list = []
while True:
    tmp_list.append(str(t % b))
    t = t // b
    if t == 0:
        break

print(int(''.join(tmp_list[::-1])))