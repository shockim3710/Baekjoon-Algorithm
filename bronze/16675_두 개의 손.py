ML, MR, TL, TR = map(str, input().split())

if ML == MR and TL == TR:
    if (ML == 'R' and TL == 'S') or (ML == 'S' and TL == 'P') or (ML == 'P' and TL == 'R'):
        print("MS")
    elif (TL == 'R' and ML == 'S') or (TL == 'S' and ML == 'P') or (TL == 'P' and ML == 'R'):
        print("TK")
    else:
        print("?")
elif ML == MR:
    if TL != ML and TR != ML:
        print("TK")
    elif ML == 'R' and (TL == 'P' or TR == 'P'):
        print("TK")
    elif ML == 'S' and (TL == 'R' or TR == 'R'):
        print("TK")
    elif ML == 'P' and (TL == 'S' or TR == 'S'):
        print("TK")
    else:
        print("?")
elif TL == TR:
    if ML != TL and MR != TL:
        print("MS")
    elif TL == 'R' and (ML == 'P' or MR == 'P'):
        print("MS")
    elif TL == 'S' and (ML == 'R' or MR == 'R'):
        print("MS")
    elif TL == 'P' and (ML == 'S' or MR == 'S'):
        print("MS")
    else:
        print("?")
else:
    print("?")