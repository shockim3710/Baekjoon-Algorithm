N, M = map(int, input().split())
A = input()
B = input()
x = 0
y = 0

for i in range(N):
    x += int(A.split(" ")[i])

for j in range(M):
    y += int(B.split(" ")[j])

print(x-y)