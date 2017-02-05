# given a list of digits, find the largest integer from those digits with the integer divisible by 3 (I think)

def answer(l):

    def list2int(l2):
        if not l2:
            return 0
        return int(''.join([str(i) for i in sorted(l2, reverse=True)]))
    m0 = list()
    m1 = list()
    m2 = list()
    for i in l:
        if i%3 == 0:
            m0.append(i)
        elif i%3 == 1:
            m1.append(i)
        elif i%3 == 2:
            m2.append(i)
    total = sum(l)
    if total % 3 == 0:
        return list2int(l)
    if total % 3 == 1:
        if m1:
            return list2int(m0 + sorted(m1, reverse=True)[:-1] + m2)
        else:
            return list2int(m0 + sorted(m2, reverse=True)[:-2])
    else:
        if m2:
            return list2int(m0 + m1 + sorted(m2, reverse=True)[:-1])
        else:
            return list2int(m0 + sorted(m1, reverse=True)[:-2])


l = [3, 1, 4, 1, 5, 9]

print(answer(l))