tk = int(input())
result = []

for i in range(tk):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))

    impLoc = [0]*N
    impLoc[M] = 'x'
    count = 0

    while True:
        if imp[0] == max(imp):
            count += 1

            if impLoc[0] == 'x':
                result.append(count)
                break

            imp.pop(0)
            impLoc.pop(0)
        else:
            imp.append(imp.pop(0))
            impLoc.append(impLoc.pop(0))

print('\n'.join(map(str, result)))


'''
    loc = imp[M]
    impSort = list(imp)
    impSort.sort(reverse=True)

    if imp.count(loc) > 1:
        numLoc = impSort[impSort.index(loc) - 1]

        if M > imp.index(numLoc):
            impSlice = imp[imp.index(numLoc):M]
            result.append(impSort.index(loc) + 1 + impSlice.count(loc))
        elif M < imp.index(numLoc):
            impSlice1 = imp[imp.index(numLoc):]
            impSlice2 = imp[:M]

            result.append(impSort.index(loc) + 1 + impSlice1.count(loc) + impSlice2.count(loc))
    else:
        result.append(impSort.index(loc)+1)

print('\n'.join(map(str, result)))
'''