N = int(input())
result = 99 # 1 ~ 99 까지는 모두 길이가 1, 2인 등차수열

if N < 100:
    print(N) # 1 ~ 99 까지는 모두 길이가 1, 2인 등차수열
else:
    for i in range(100, N+1):
        num = list(str(i)) # 각 자리수 하나하나를 리스트에 저장
        compar = int(num[1]) - int(num[0]) # 십의자리수 - 일의자리수

        for j in range(len(num)-2):
            if int(num[j+2]) - int(num[j+1]) != compar:
                break # (백의자리수 - 십의자리수)가 compar와 같지 않다면 중지
            result += 1 # 모든 길이가 같으면 result에 1 더함

    print(result)