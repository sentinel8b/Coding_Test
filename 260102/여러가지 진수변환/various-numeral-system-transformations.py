N, B = map(int, input().split())

# Please write your code here.

div_list = []

while True:
    div_list.append(str(N % B))
    N = N // B
    if N == 0:
        break

result = ''.join(div_list[::-1])

print(int(result))