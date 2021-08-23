N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start, end = 0, max(budget)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in budget:
        if i > mid:
            count += mid
        else:
            count += i

    if count > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)