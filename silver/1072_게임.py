import sys

X, Y = map(int, sys.stdin.readline().split())

Z = int((Y * 100 / X)) # 실수오차
start, end = 0, 1000000000
result = 0

if Z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2

        if int(((Y + mid) * 100 / (X + mid))) > Z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)

