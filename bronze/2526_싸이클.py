N, P = map(int, input().split())
x = N
result = 0
cyc = []

for i in range(1000):
    result = (x * N) % P

    if result in cyc:
        break
    else:
        cyc.append(result)
        x = result

print(len(cyc)-cyc.index(result))