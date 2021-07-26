N, K = map(int, input().split())
g = []
s = []
b = []
found = []
count = 0

for i in range(N):
    Num, G, S, B = map(int, input().split())
    if Num == K:
        found.append(G)
        found.append(S)
        found.append(B)
    else:
        g.append(G)
        s.append(S)
        b.append(B)

for i in range(N-1):
    if found[0] == max(g) or found[0] == g[i]:
        if found[1] == max(s) or found[1] == s[i]:
            if found[2] == max(b) or found[2] == b[i]:
                continue
            elif found[2] < b[i] and found[0] == g[i] and found[1] == s[i]:
                count += 1
        elif found[1] < s[i] and found[0] == g[i]:
            count += 1
    elif found[0] < g[i]:
        count += 1

print(count+1)