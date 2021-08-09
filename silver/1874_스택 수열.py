n = int(input())

stackList = []
num = []
stack = []
result = []

for i in range(n):
    stackList.append(int(input()))
    num.append(i+1) # 1부터 n까지 num에 추가

while len(num) != 0: # num의 배열이 빌 때까지 반복
    stack.append(num.pop(0))
    # num의 0번째 인덱스를 pop하고 stack에 추가
    result.append('+')

    while True:
        if stack[-1] == stackList[0]:
            # stack 마지막 인덱스와 stackList 0번째 인덱스가 같으면 pop
            stack.pop(-1)
            stackList.pop(0)
            result.append('-')

            if len(stack) == 0: # stack이 비어있으면 멈춤
                break
        else:
            break

if len(stack) == 0:
    print('\n'.join(map(str, result)))
else: # stack이 비어있지 않으면 불가능한 경우이므로 NO를 출력
    print('NO')