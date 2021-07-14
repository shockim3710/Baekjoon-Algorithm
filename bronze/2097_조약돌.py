import sys

N = int(sys.stdin.readline())
x = 0
y = 0

while True:
    if (x+2)*(y+2) >= N:
        print(((x+1)*2)+((y+1)*2))
        break
    else:
        if x == y:
            x += 1
        else:
            y += 1