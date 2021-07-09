N = int(input())
Pi = input()

result = []
olm = []
olmLeg = [0]

for i in range(N):
    x = int(Pi.split(" ")[i])
    result.append(x)

for i in range(N-1):
    if result[i] < result[i+1]:
        olm.append(result[i])
        olm.append(result[i+1])
        if i == N-2:
            olmLeg.append(max(olm)-min(olm))
    else:
        if len(olm) != 0:
            olmLeg.append(max(olm)-min(olm))
            olm = []

print(max(olmLeg))