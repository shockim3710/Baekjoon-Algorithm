T = int(input())
result1 = []
result2 = []

for i in range(T):
    H, W, N = map(int, input().split())
    if N%H == 0:
        result1.append(H)
        result2.append(N//H)
    else:
        result1.append(N%H)
        result2.append(N//H+1)

for i in range(T):
    if result2[i] < 10:
        print("{}0{}".format(result1[i], result2[i]))
    else:
        print("{}{}".format(result1[i], result2[i]))