N = int(input())
t = []
p = []
dp = [0]*(N+1)

for i in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(N-1, -1, -1):
    if t[i]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(dp[0])


'''
N = int(input())
t = []
p = []
result = []

for i in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(N):
    count = i
    money = 0
    for j in range(N-i):
        countNum = count
        money += p[count]
        count += t[count]

        if count == N:
            break
        elif count > N-1:
            money -= p[countNum]
            break

    result.append(money)

print(max(result))
'''