n = []
a = []
x = []
high = [10]
low = [0]

while True:
    num = int(input())
    if num == 0:
        break
    ans = input()

    n.append(num)
    a.append(ans)

    if ans == 'right on':
        for i in range(len(n)-1):
            if a[i] == 'too high':
                high.append(n[i])
            elif a[i] == 'too low':
                low.append(n[i])

        if len(high) == 1 and len(low) == 1:
            x.append(0)
        elif len(high) == 1 and n[-1] > max(low):
            x.append(0)
        elif len(low) == 1 and n[-1] < min(high):
            x.append(0)
        elif max(low) < n[-1] < min(high):
            x.append(0)
        else:
            x.append(-1)

        n = []
        a = []
        high = [10]
        low = [0]

for i in range(len(x)):
    if x[i] == -1:
        print('Stan is dishonest')
    else:
        print('Stan may be honest')



'''
n = []
a = []
x = []

while True:
    num = int(input())
    if num == 0:
        break
    ans = input()

    n.append(num)
    a.append(ans)
    k = 0

    if ans == 'right on':
        for i in range(len(n)-1):
            if (n[i] < n[-1] and a[i] == 'too high') or (n[i] > n[-1] and a[i] == 'too low'):
                k = -1
                break

        x.append(k)
        n = []
        a = []

for i in range(len(x)):
    if x[i] == -1:
        print('Stan is dishonest')
    else:
        print('Stan may be honest')
'''