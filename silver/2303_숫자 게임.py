N = int(input())
result = []

for i in range(N):
    c = list(map(int, input().split()))
    num = []
    
    for j in range(5):
        for k in range(j+1, 5):
            for l in range(k+1, 5):
                num.append((c[j]+c[k]+c[l])%10)

    result.append(max(num))

result.reverse()
print(N - result.index(max(result)))