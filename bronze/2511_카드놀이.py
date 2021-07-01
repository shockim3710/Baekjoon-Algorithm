A = list(map(int, input().split()))
B = list(map(int, input().split()))

Ascore = 0
Bscore = 0
Alist = 0
Blist = 0

for i in range(10):
    if A[i] > B[i]:
        Ascore += 3
        Alist = i

    elif A[i] < B[i]:
        Bscore += 3
        Blist = i

    else:
        Ascore += 1
        Bscore += 1

print(Ascore, Bscore)

if Ascore > Bscore:
    print("A")
elif Ascore < Bscore:
    print("B")
elif Ascore == Bscore:

    if Alist > Blist:
        print("A")
    elif Alist < Blist:
        print("B")
    else:
        print("D")
