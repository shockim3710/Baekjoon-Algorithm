N, M = map(int, input().split())
order = []
dice = []
locate = 0
move = 0
count = 0

for i in range(N):
    X = int(input())
    order.append(X)
for i in range(M):
    Y = int(input())
    dice.append(Y)

for i in range(M):
    if locate + dice[i] < N:
        move = order[dice[i]+locate]
        locate += dice[i]+move
        count += 1
        if locate+1 >= N:
            break
    else:
        count += 1
        break

print(count)