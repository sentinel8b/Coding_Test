N = input()

# Please write your code here.
t = 0
for i in range(len(N[::-1])):
    t += 2 ** i * int(N[::-1][i])

result_t = t * 17

bin_list = []
while True:
    bin_list.append(str(result_t % 2))
    result_t = result_t // 2
    if result_t == 0:
        break

print(int(''.join(bin_list[::-1])))