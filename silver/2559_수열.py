import sys

N, K = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

accSum = [temp[0]]
result = []
startDate, endDate = 0, K-1

for i in range(len(temp)-1):
    accSum.append(accSum[i]+temp[i+1])

while endDate < len(temp) or startDate < 0:
    if startDate-1 == -1:
        result.append(accSum[endDate])
    else:
        result.append(accSum[endDate] - accSum[startDate - 1])

    startDate += 1
    endDate += 1

print(max(result))