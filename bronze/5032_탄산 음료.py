e, f, c = map(int, input().split())
e += f

result = 0
remain = 0
count = 0

while (e+remain) // c != 0:
    result = (e+remain) // c

    e = (e+remain) % c
    remain = result
    count += result

print(count)