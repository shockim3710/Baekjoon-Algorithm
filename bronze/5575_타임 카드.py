num1 = input()
num2 = input()
num3 = input()

Ah1 = int(num1.split(" ")[0])
Am1 = int(num1.split(" ")[1])
As1 = int(num1.split(" ")[2])
Ah2 = int(num1.split(" ")[3])
Am2 = int(num1.split(" ")[4])
As2 = int(num1.split(" ")[5])

Bh1 = int(num2.split(" ")[0])
Bm1 = int(num2.split(" ")[1])
Bs1 = int(num2.split(" ")[2])
Bh2 = int(num2.split(" ")[3])
Bm2 = int(num2.split(" ")[4])
Bs2 = int(num2.split(" ")[5])

Ch1 = int(num3.split(" ")[0])
Cm1 = int(num3.split(" ")[1])
Cs1 = int(num3.split(" ")[2])
Ch2 = int(num3.split(" ")[3])
Cm2 = int(num3.split(" ")[4])
Cs2 = int(num3.split(" ")[5])

A1 = Ah2-Ah1
A2 = Am2-Am1
A3 = As2-As1

B1 = Bh2-Bh1
B2 = Bm2-Bm1
B3 = Bs2-Bs1

C1 = Ch2-Ch1
C2 = Cm2-Cm1
C3 = Cs2-Cs1

if A3 < 0:
    A3 = 60 + A3
    A2 -= 1

if A2 < 0:
    A2 = 60 + A2
    A1 -= 1

if B3 < 0:
    B3 = 60 + B3
    B2 -= 1

if B2 < 0:
    B2 = 60 + B2
    B1 -= 1

if C3 < 0:
    C3 = 60 + C3
    C2 -= 1

if C2 < 0:
    C2 = 60 + C2
    C1 -= 1

print(A1, A2, A3)
print(B1, B2, B3)
print(C1, C2, C3)