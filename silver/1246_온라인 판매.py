N, M = map(int, input().split())
Pi = []
result = []

for i in range(M):
    Pi.append(int(input()))

Pi.sort()
count = M

for i in range(M):
    if N < count:
        result.append(Pi[i] * N)
        count -= 1
    else:
        result.append(Pi[i]*count)
        count -= 1

print(Pi[result.index(max(result))], max(result))
