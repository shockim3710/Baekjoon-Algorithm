n = int(input())
f1 = 0
f2 = 1
result = 0

for i in range(n-1):
    result = f1 + f2
    f1 = f2
    f2 = result

if n == 1:
    print(1)
else:
    print(result)