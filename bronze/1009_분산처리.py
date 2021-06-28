T = int(input())
result = []

for i in range(T):
    a, b = map(int, input().split())
    a = a % 10
    # a의 b 제곱수를 추가하면 시간초과가 나므로
    # a 제곱수를 나열하여 1의자리 숫자의 규칙을 적용

    if a == 0:
        # 10 제곱수 = 1'0', 10'0', 100'0'
        result.append(10)
    elif a == 1 or a == 5 or a == 6:
        # 1 제곱수 =  '1', '1', '1'
        # 5 제곱수 = '5', 2'5', 12'5'
        # 6 제곱수 = '6', 3'6', 21'6'
        result.append(a)
    elif a == 4 or a == 9:
        # 4 제곱수 = '4', 1'6', 6'4'
        # 9 제곱수 = '9', 8'1', 72'9'
        if b % 2 != 0:
            result.append(a)
        else:
            result.append((a * a) % 10)
    else:
        # 2 제곱수 = '2', '4', '8', 1'6', 3'2'
        # 3 제곱수 = '3', '9', 2'7', 8'1', 24'3'
        # 7 제곱수 = '7', 4'9', 34'3', 240'1', 1680'7'
        # 8 제곱수 = '8', 6'4', 51'2', 409'6', 3276'8'
        b = b % 4

        if b == 0:
            result.append((a**4) % 10 % 10 % 10)
        else:
            result.append((a**b) % 10 % 10 % 10)

print('\n'.join(map(str, result)))