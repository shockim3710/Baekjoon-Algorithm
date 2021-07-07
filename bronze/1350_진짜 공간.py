N = int(input())
F = input()
f = []
count = 0

for i in range(N):
    x = int(F.split(" ")[i])
    f.append(x)

c = int(input())

for i in range(N):
    if f[i] > c:
        if f[i]%c == 0:
            count += f[i]//c
        else:
            count += 1+(f[i]//c)
    elif f[i] == 0:
        continue
    else:
        count += 1

print(c*count)