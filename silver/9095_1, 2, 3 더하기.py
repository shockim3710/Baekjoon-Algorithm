T = int(input())

result = [1, 2, 4]
testCaseResult = []

'''
n, 방법의 수
1, 1
2, 2
3, 4
4, 1+2+4 = 7
5, 2+4+7 = 13

따라서 n이 4일 때부터 그 전, 전전, 전전전 수의 합이 방법의 수가 됨
'''
for i in range(4, 11): # 미리 1부터 10까지의 방법의 수를 저장
    result.append(result[i-4] + result[i-3] + result[i-2])

for i in range(T): # n-1의 위치에 저장된 방법의 수를 출력
    testCaseResult.append(result[int(input())-1])

print('\n'.join(map(str, testCaseResult)))