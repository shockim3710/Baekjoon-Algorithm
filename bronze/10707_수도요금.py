A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A*P

if C<P:
    Y = B+(P-C)*D
else:
    Y = B

if X<Y:
    print(X)
else:
    print(Y)