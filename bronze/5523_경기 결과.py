import sys

N = int(input())
Awin = 0
Bwin = 0

for i in range(N):
    Ai, Bi = map(int, sys.stdin.readline().split())

    if Ai > Bi:
        Awin += 1

    elif Ai < Bi:
        Bwin += 1

print(Awin, Bwin)