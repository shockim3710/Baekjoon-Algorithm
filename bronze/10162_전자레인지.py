T = int(input())
A = 0
B = 0
C = 0

if T >= 300:
    A = int(T / 300)

    if T % 300 >= 60:
        B = int(T % 300 / 60)

    if T % 300 % 60 % 10 == 0:
        C = int(T % 300 % 60 / 10)
        print(A, B, C)

    else:
        print(-1)

elif T >= 60:
    B = int(T / 60)

    if T % 60 % 10 == 0:
        C = int(T % 60 / 10)
        print(A, B, C)

    else:
        print(-1)

elif T >= 10:
    if T % 10 == 0:
        C = int(T / 10)
        print(A, B, C)

    else:
        print(-1)

else:
    print(-1)