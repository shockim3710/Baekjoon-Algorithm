T = int(input())
a = []
b = []
c = []

for i in range(T):
    A, B, C = list(map(int, input().split()))
    a.append(A)
    b.append(B)
    c.append(C)

for i in range(T):
    if a[i] == b[i] == c[i]:
        print("Case #{}: equilateral".format(i+1))

    elif max(a[i], b[i], c[i]) < a[i]+b[i]+c[i]-max(a[i], b[i], c[i]):
        if a[i] == b[i] or a[i] == c[i] or b[i] == c[i]:
            print("Case #{}: isosceles".format(i+1))

        else:
            print("Case #{}: scalene".format(i+1))

    else:
        print("Case #{}: invalid!".format(i+1))