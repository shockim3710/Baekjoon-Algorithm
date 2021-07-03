K = int(input())
N = int(input())
time = 0

for i in range(N):
    T, Z = map(str, input().split())
    time += int(T)

    if time < 210:
        if Z == 'T':
            K += 1
            if K == 9:
                K = 1
    else:
        break

print(K)