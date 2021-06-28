N = int(input())

file = [[] * N for i in range(N)] # N만큼 2중리스트 생성
result = []

for i in range(N): # 파일 이름을 리스트에 저장
    file[i].extend(list(input()))

for i in range(len(file[0])):
    count = 0

    for j in range(N-1):
        # 각각의 자리를 비교하여 같지 않으면, count를 하고 break
        if file[j][i] != file[j+1][i]:
            count = 1
            break

    if count == 0: # count가 안되었으면 그 글자를 result 배열에 추가
        result.append(file[0][i])
    else: # count가 되었으면 ?를 result 배열에 추가
        result.append('?')

print(''.join(result)) # result 배열에 저장된 글자를 합쳐 출력