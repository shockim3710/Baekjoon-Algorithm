from itertools import permutations

n = int(input())
k = int(input())
card = []
result = set()

for i in range(n):
    card.append(str(input()))

change = list(set(permutations(card, k)))

for i in range(len(change)):
    x = '0'
    for j in range(k):
        x += change[i][j]

    result.add(int(x))

print(len(result))