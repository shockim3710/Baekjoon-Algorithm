K, N = map(int, input().split())
LAN = []

for i in range(K):
    LAN.append(int(input()))

start, end = 1, max(LAN)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in LAN:
        count += i // mid

    if count < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)