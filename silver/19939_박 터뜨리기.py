N, K = map(int, input().split())
num = 0
result = 0

for i in range(1, K+1):
    num += i

if N < num:
    result = -1
else:
    if num % K == N % K:
        result = K - 1
    else:
        result = K

print(result)