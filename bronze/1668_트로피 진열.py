N = int(input())
save1 = [0]
save2 = [0]
maxSave1 = [0]
maxSave2 = [0]
count1 = 0
count2 = 0

for i in range(1, N+1):
    t = int(input())
    save1.append(t)

    if save1[i] >= max(save1) and save1[i] != max(maxSave1):
        maxSave1.append(max(save1))
        count1 += 1
    else:
        continue
print(count1)

save1.reverse()
save1.remove(0)

for i in range(1, N+1):
    save2.append(save1[i-1])

    if save2[i] >= max(save2) and save2[i] != max(maxSave2):
        maxSave2.append(max(save2))
        count2 += 1
    else:
        continue
print(count2)