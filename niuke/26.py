import sys
lines = sys.stdin.readlines()
a1 = list(map(int,lines[0].strip().split()))
if len(lines) == 1:
    str_ = ''
    for a_ in a1:
        str_ += (str(a_) + ',')
    print(str_.strip())
else:
    a2 = list(map(int,lines[1].strip().split()))
    str_ = []
    ind1 = 0
    ind2 = 0

    while True:
        if ind1 >= len(a1):
            out += a2[ind2:]
            break
        if ind2 >= len(a2):
            out += a1[ind1:]
            break
        if a1[ind1] <= a2[ind2]:
            out.append(a1[ind1])
            ind1 += 1
        else:
            out.append(a2[ind2])
            ind2 += 1
    str_ = ''
    for a_ in out:
        str_ += (str(a_) + ',')
    print(str_.strip())