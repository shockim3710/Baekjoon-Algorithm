N = int(input())

num1, num2 = 1, 2
result = 0

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    for i in range(N-2):
        result = (num1 + num2) % 15746
        num1 = num2
        num2 = result

    print(result)