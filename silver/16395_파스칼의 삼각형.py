n, k = map(int, input().split())
resultN, resultK, resultNK = 1, 1, 1

for i in range(1, n):
    resultN *= i
for j in range(1, k):
    resultK *= j
for l in range(1, n-k+1):
    resultNK *= l

print(resultN // (resultK * resultNK))