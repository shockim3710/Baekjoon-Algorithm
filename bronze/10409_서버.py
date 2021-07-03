n, T = map(int, input().split())
x = input()
z = []
result = 0
num = 0

for i in range(n):
    y = int(x.split(" ")[i])
    z.append(y)
    result += z[i]

    if result <= T:
        num = i+1

    elif result > T:
        num = i
        break

print(num)