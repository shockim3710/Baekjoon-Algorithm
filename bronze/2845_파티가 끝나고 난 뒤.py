num1 = input()
num2 = input()

L = int(num1.split(" ")[0])
P = int(num1.split(" ")[1])

people1 = int(num2.split(" ")[0])
people2 = int(num2.split(" ")[1])
people3 = int(num2.split(" ")[2])
people4 = int(num2.split(" ")[3])
people5 = int(num2.split(" ")[4])

if 1 <= L <= 10 and 1 <= P <= 1000:
    result = L * P

if 0 <= people1 < 10E6:
    print(people1 - result)

if 0 <= people2 < 10E6:
    print(people2 - result)

if 0 <= people3 < 10E6:
    print(people3 - result)

if 0 <= people4 < 10E6:
    print(people4 - result)

if 0 <= people5 < 10E6:
    print(people5 - result)