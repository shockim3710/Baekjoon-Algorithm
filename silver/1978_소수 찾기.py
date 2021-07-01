N = int(input())
a = input()

k = []
result = 0

for i in range(N):
    b = int(a.split(" ")[i])
    k.append(b)

for i in range(N):
    count = 0

    for j in range(k[i]):

        if k[i] % (j + 1) == 0:
            count += 1

    if count == 2:
        result += 1

print(result)
