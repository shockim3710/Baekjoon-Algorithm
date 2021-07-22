K = int(input())
max_num = []
min_num = []
gap_num = []

for i in range(K):
    x = list(map(int, input().split()))
    x.remove(x[0])
    gap = []

    max_num.append(max(x))
    min_num.append(min(x))
    x.sort(reverse=True)

    for j in range(len(x)-1):
        gap.append(abs(x[j]-x[j+1]))

    gap_num.append(max(gap))

for i in range(K):
    print('Class', i+1)
    print('Max {}, Min {}, Largest gap {}'.format(max_num[i], min_num[i], gap_num[i]))