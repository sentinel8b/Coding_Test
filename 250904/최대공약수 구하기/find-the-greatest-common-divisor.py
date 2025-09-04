n, m = map(int, input().split())

# Please write your code here.
def get_gcd(n,m):
    for i in range(min(n,m),1, -1):
        if n % i == 0 and m % i ==0:
            print(i)
            exit()

get_gcd(n,m)