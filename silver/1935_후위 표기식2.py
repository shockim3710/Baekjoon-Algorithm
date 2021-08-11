N = int(input())
pn = list(input().strip())

num = []
alpha = []
numPop = []

for i in range(N):
    num.append(int(input()))

for i in range(len(pn)):
    if pn[0].isupper():
        numPop.append(num[ord(pn[0]) - ord('A')])
        alpha.append(pn.pop(0))

    else:
        if pn[0] == '+':
            numPop.append(numPop.pop(-2) + numPop.pop(-1))
        elif pn[0] == '-':
            numPop.append(numPop.pop(-2) - numPop.pop(-1))
        elif pn[0] == '*':
            numPop.append(numPop.pop(-2) * numPop.pop(-1))
        elif pn[0] == '/':
            numPop.append(numPop.pop(-2) / numPop.pop(-1))

        pn.pop(0)

print("%0.2f" % numPop[0])