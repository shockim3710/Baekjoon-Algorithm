n = int(input())
m = int(input())
count = 0
result = []

for i in range(n):
    inCar, outCar = map(int, input().split())
    m += inCar
    m -= outCar

    if m < 0:
        count += 1
    else:
        result.append(m)

if count > 0:
    print(0)
else:
    print(max(result))
