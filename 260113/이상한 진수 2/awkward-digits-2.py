a = input()

# Please write your code here.

def bin2dec(bin):
    dec = 0
    for idx in range(len(bin)):
        dec += int(bin[::-1][idx]) * 2 ** idx
    return dec

count = 0
for idx in range(len(a)):
    if a[idx] == '0':
        break
    else:
        count += 1
if count == len(a):
    bin = ''.join([a[:idx], '0'])
else:
    bin = ''.join([a[:idx], '1', a[idx+1:]])

print(bin2dec(bin))