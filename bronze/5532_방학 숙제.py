L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

x = int(A/C)
y = int(B/D)

if A%C != 0:
    x += 1

if B%D != 0:
    y += 1

if x>y:
    print(L-x)

else:
    print(L-y)