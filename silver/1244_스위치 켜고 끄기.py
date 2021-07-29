sCount = int(input())
switch = list(map(int, input().split()))
pCount = int(input())

for i in range(pCount):
    gender, num = map(int, input().split())
    numCount = num

    if gender == 1:
        for j in range(sCount//num):
            if switch[num-1] == 0:
                switch[num-1] = 1
            else:
                switch[num-1] = 0

            num += numCount

    elif gender == 2:
        count = 1

        while True:
            if (num-1)-count < 0 or (num-1)+count >= len(switch):
                if switch[num-1] == 0:
                    switch[num-1] = 1
                else:
                    switch[num-1] = 0

                break
            elif switch[(num-1)-count] != switch[(num-1)+count]:
                if switch[num-1] == 0:
                    switch[num-1] = 1
                else:
                    switch[num-1] = 0

                break
            elif switch[(num-1)-count] == switch[(num-1)+count]:
                if switch[(num-1)-count] == 0:
                    switch[(num-1)-count], switch[(num-1)+count] = 1, 1
                else:
                    switch[(num-1)-count], switch[(num-1)+count] = 0, 0

                count += 1

for i in range(1, len(switch)+1):
    print(switch[i - 1], end=' ')
    if i % 20 == 0:
        print('')