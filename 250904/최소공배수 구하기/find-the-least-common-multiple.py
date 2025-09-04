n, m = map(int, input().split())

# Please write your code here.
def LCM(n, m):
    max_val = max(n,m)
    while True:
        if max_val % n == 0 and max_val % m == 0:
            print(max_val)
            exit()
        else:
            max_val += 1

LCM(n,m)