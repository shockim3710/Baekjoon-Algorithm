num = input()
N = int(num.split(" ")[0])
T = int(num.split(" ")[1])
C = int(num.split(" ")[2])
P = int(num.split(" ")[3])

x = int(N/T)

if N%T == 0:
    print((x-1)*C*P)
else:
    print(x*C*P)