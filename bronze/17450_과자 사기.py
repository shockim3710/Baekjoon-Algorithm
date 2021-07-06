result = []

for i in range(3):
    price, weight = map(int, input().split())

    if price*10 >= 5000:
        price = price*10 - 500
    else:
        price *= 10

    weight *= 10
    result.append(weight/price)

if max(result) == result[0]:
    print("S")
elif max(result) == result[1]:
    print("N")
elif max(result) == result[2]:
    print("U")