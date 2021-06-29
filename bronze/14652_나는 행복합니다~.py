num = input()
N = int(num.split(" ")[0])
M = int(num.split(" ")[1])
K = int(num.split(" ")[2])

x = int(K/M)
y = int(K%M)

print(x, y)