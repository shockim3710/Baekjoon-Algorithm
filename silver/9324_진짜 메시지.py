import sys

n = int(input())
result = []

for i in range(n):
    M = list(sys.stdin.readline())
    mList = []

    mess = list(set(M))
    tfCount = 0

    for j in range(len(mess)):
        count3 = 0
        for k in range(len(M)):
            if mess[j] == M[k]:
                count3 += 1

                if count3 % 3 == 0 and k == len(M)-1:
                    tfCount += 1
                    break
                if count3 % 3 == 0 and M[k] != M[k+1]:
                    tfCount += 1
                    break

                if count3 == 4:
                    count3 = 0

        if tfCount == 1:
            break

    if tfCount > 0:
        result.append('FAKE')
    else:
        result.append('OK')

print("\n".join(result))