num = int(input())

grade = [[], [], [], [], []]
stu = {}
result = []

for i in range(num):
    ban = list(map(int, input().split()))
    stu[i + 1] = []

    for j in range(5):
        grade[j].append(ban[j])

for i in range(num):
    for j in range(5):
        for k in range(num):
            if grade[j][i] == grade[j][k]:
                stu[i+1].append(k+1)

for i in range(num):
    result.append(len(set(stu[i+1])))

print(result.index(max(result))+1)