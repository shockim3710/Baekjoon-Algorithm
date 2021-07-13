a, b, c, d, e, f = map(int, input().split())
x = 0
y = 0

if a == 0 or d == 0:
    newB = b * d
    newC = c * d
    newE = e * a
    newF = f * a
    y = (newC - newF) / (newB - newE)

    if a == 0:
        x = (f - (e * y)) / d
    elif d == 0:
        x = (c - (b * y)) / a

else:
    newA = a * e
    newC = c * e
    newD = d * b
    newF = f * b
    x = (newC - newF) / (newA - newD)

    if b == 0:
        y = (f - (d * x)) / e
    else:
        y = (c - (a * x)) / b

print(int(x), int(y))