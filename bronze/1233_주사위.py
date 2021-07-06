x, y, z = map(int, input().split())
result1 = []
result2 = []
result3 = []

for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            result1.append(i+j+k)

for i in range(3, x+y+z+1):
    result2.append(result1.count(i))
    result3.append(i)

print(result3[result2.index(max(result2))])