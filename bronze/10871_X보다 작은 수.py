N, X = map(int, input().split())
A = input()
x = []

for i in range(N):
    a = int(A.split(" ")[i])

    if a < X:
        print(a, end=' ')
