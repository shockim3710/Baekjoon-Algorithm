N = int(input())
m = []
k = []
num = []

for i in range(N):
    x, y = map(int, input().split())
    m.append(x)
    k.append(y)

for i in range(N):
    count = 0
    
    for j in range(N):
        if m[i] < m[j] and k[i] < k[j]:
            count += 1

    num.append(count+1)

print(" ".join(map(str, num)))