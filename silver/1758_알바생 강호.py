N = int(input())
tip = []
money = 0
result = 0

for i in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)

for i in range(N):
    money = tip[i] - ((i+1)-1)
    if money > 0:
        result += money

print(result)