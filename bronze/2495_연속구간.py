result = []

for i in range(3):
    x = list(input())
    z = [0]
    count = 0

    for j in range(7):
        if x[j] == x[j+1]:
            count += 1
            z.append(count)
        else:
            count = 0

    if max(z) == 0 and min(z) == 0:
        result.append(1)
    else:
        result.append(max(z)+1)

for i in range(3):
    print(result[i])