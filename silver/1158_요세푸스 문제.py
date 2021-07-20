N, K = map(int, input().split())
num = []
result = []
K -= 1
x = K

num = [i for i in range(1, N+1)]

for i in range(N):
    result.append(num[K])
    num.pop(K)
    K += x

    if i == N-1:
        break
    elif K >= len(num):
        K = K%len(num)

for i in range(N):
    if len(result) == 1:
        print('<{}>'.format(result[i]))
    elif i == 0:
        print('<{}, '.format(result[i]), end='')
    elif i == N-1:
        print('{}>'.format(result[i]))
    else:
        print('{}, '.format(result[i]), end='')