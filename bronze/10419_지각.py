T = int(input())
x = []
result = 0

for i in range(T):
    d = int(input())
    x.append(d)

for i in range(T):
    for j in range(x[i]):
        if j+(j**2) <= x[i]:
            result = j

    print(result)