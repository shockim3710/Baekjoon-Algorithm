n = int(input())
h = list(input())

num = []
hiddenNum = []
result = 0

for i in range(n):
    if h[i].isdigit() == True: # 단어 하나가 숫자이면 num에 추가
        num.append(h[i])
    else:
        # 숫자가 아니면 string으로 num에 저장된 숫자를 x에 더하여
        # 하나의 숫자로 만들어 hiddenNum에 추가
        x = '0'
        for i in range(len(num)):
            x += num[i]
        hiddenNum.append(int(x))
        num = []

if len(num) > 0:
    # num의 배열이 비어있지 않으면 저장된 숫자를 하나의 숫자로 만듦
    x = '0'
    for i in range(len(num)):
        x += num[i]
    hiddenNum.append(int(x))

if len(hiddenNum) == 0: # 히든 넘버가 없는 경우, result에 0을 저장
    result = 0
else: # 히든 넘버가 있는 경우, result에 모두 더함
    for i in range(len(hiddenNum)):
        result += hiddenNum[i]

print(result)