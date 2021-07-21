result = []

while True:
    L, P, V = map(int, input().split())
    num = 0

    if L == 0 and P == 0 and V == 0:
        break
    else:
        x = V // P
        num = L * x

        y = V % P
        if y < L:
            num += y
        else:
            num += L

        result.append(num)

for i in range(len(result)):
    print('Case {}: {}'.format(i+1, result[i]))