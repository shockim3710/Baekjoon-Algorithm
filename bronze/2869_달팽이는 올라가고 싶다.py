import math

A, B, V = map(int, input().split())
# 낮과 밤을 합쳐서 오를 미터를 소수점 올림으로 저장
result = math.ceil(V / (A - B))

# 만약 마지막 밤에 미끄러진 미터를 제외한 결과가 result 보다 작으면
# 그 값을 출력
if result > (V - B) / (A - B):
    print(math.ceil((V - B) / (A - B)))
else:
    print(result)