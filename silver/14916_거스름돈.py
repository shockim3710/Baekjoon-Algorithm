n = int(input())
count = n // 5

if n == 1 or n == 3:
    count = -1
elif n % 5 == 0:
    pass
elif (n % 5) % 2 == 0:
    x = (n % 5) // 2
    count += x
else:
    x = ((n % 5)+5) // 2
    count += (x-1)

print(count)