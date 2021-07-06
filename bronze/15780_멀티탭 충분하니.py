N, K = map(int, input().split())
A = input()
result = 0

for i in range(K):
    x = int(A.split(" ")[i])

    if x == 3 or x == 4:
        result += 2
    elif x == 5 or x == 6:
        result += 3
    elif x == 7 or x == 8:
        result += 4

if N <= result:
    print("YES")
else:
    print("NO")