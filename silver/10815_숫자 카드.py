import sys

N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
x = list(map(int, sys.stdin.readline().split()))

maxAList = max(A)

for i in range(M):
    if x[i] > maxAList:
        print(0, end=' ')
    elif x[i] in A:
        print(1, end=' ')
    else:
        print(0, end=' ')