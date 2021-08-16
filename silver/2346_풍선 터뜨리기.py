N = int(input())
balloon = list(map(int, input().split()))

num = []
result = [1]

for i in range(2, N+1):
    num.append(i)

move = balloon.pop(0)
loc = 0

for i in range(N-1):
    if move < 0:
        loc = (loc + move) % len(balloon)
    else:
        loc = (loc + (move-1)) % len(balloon)

    result.append(num.pop(loc))
    move = balloon.pop(loc)

print(' '.join(map(str, result)))