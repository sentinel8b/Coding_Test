binary = input()

# Please write your code here.

result = 0
bin_list = []

for b in binary[::-1]:
    bin_list.append(int(b))

for i in range(len(bin_list)):
    result += 2 ** i * bin_list[i]

print(result)