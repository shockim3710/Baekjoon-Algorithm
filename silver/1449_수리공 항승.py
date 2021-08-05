N, L = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

result = 1
start = loc[0]
end = loc[0] + L

for i in range(N):
    if start <= loc[i] < end:
        continue
    else:
        start = loc[i]
        end = loc[i] + L
        result += 1

print(result)



'''
N, L = map(int, input().split())
loc = list(map(int, input().split()))

count = 0
result = 0
check1 = 0
check2 = 0

if L == 1:
    result = N
elif N == 1:
    result = 1
else:
    for i in range(N - 1):
        if abs(loc[i + 1] - loc[i]) < L - 1:
            count += 1
            if count == L - 1:
                result += 1
                count = 0

        elif abs(loc[i + 1] - loc[i]) == L - 1:
            result += 1
            if L == 2:
                check1 += 1

        elif abs(loc[i + 1] - loc[i]) > L - 1:
            check2 += 1

    if count > 0:
        result += 1
    if abs(loc[-1] - loc[-2]) > L - 1:
        result += 1
    if check1 == N-1:
        result -= 1
    if check2 == N - 1:
        result = N

print(result)
'''