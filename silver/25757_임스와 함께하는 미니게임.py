import sys

N, g = map(str, sys.stdin.readline().split())
peopleList = set() # 중복 인원 제거

for i in range(int(N)):
    peopleList.add(sys.stdin.readline().replace("\n", ""))

# 임스를 포함하여 미니게임
if str(g) == "Y":
    print(len(peopleList))
elif str(g) == "F":
    print(len(peopleList) // 2)
elif str(g) == "O":
    print(len(peopleList) // 3)
