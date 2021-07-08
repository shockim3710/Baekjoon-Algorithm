N, M = map(int, input().split())
c = input()
card = []
hap = []

for i in range(N):
    x = int(c.split(" ")[i])
    card.append(x)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            hap.append(card[i]+card[j]+card[k])

if M in hap:
    print(M)
else:
    hap.append(M)
    hap.sort()
    print(hap[hap.index(M)-1])