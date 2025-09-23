N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)] # t, x, y

infected = {P : K}

status = [0] * (N+1)

# Sort handshake by time order
handshakes = sorted(handshakes, key = lambda x : (x[0], x[1], x[2]))

# Iterate over handsakes following time order
for t, x, y in handshakes:
    # If x is infected who has remains
    initially_added = False
    if x in infected.keys():
        if infected[x] > 0:
            infected[x] -= 1
            # Add y to infected
            if y not in infected.keys():
                infected[y] = K
                initially_added = True
    # If x is infected who has remains          
    if not initially_added:
        if y in infected.keys():
            if infected[y] > 0:
                infected[y] -= 1
                # Add y to infected
                if x not in infected.keys():
                    infected[x] = K

# Trace who is infected
for i in range(1, N+1):
    if i in infected.keys():
        print(1, end = "")
    else:
        print(0, end = "")



