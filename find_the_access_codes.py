import random

# find triples (li,lj,lk) st i<j<k and li|lj and lj|lk


# MISREAD QUESTION OOPS
def answer(l):
    tot=0
    l_div = [0]
    for i in range(1, len(l)):
        divisors = 0
        for j in range(i):
            if l[i] % l[j] == 0:
                divisors += 1
                tot += l_div[j]
        l_div.append(divisors)

    return tot


# one of my many misinterpretations of the question

def answer2(l):
    n = len(l)
    l2 = sorted(l)
    unique = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if l2[j]%l2[i] == 0 and l2[k]%l2[j] == 0:
                    unique.add((l2[i], l2[j], l2[k]))
    return len(unique)


def answer3(l):
    tot = 0
    dup = dict()

    dup[l[0]] = 0
    for i in range(1, len(l)):
        if l[i] in dup:
            dup[l[i]] += 1
        else:
            dup[l[i]] = 0

    unique = sorted(dup.keys())

    l_div = [0]
    for i in range(1, len(unique)):
        divisors = 0
        for j in range(i):
            if unique[i] % unique[j] == 0:
                divisors += 1
                # abc
                tot += l_div[j]

                # aab
                if dup[unique[j]] > 0:
                    tot += 1

                # abb
                if dup[unique[i]] > 0:
                    tot += 1
        l_div.append(divisors)

    # aaa
    for i in dup.values():
        if i >= 2:
            tot += 1

    return tot

for i in range(100000):
    l = [random.randint(5,15) for i in range(5)]
    if answer(l) != answer2(l):
        print(l)
        print(answer(l), answer2(l))
        break

# print(answer([random.randint(1,10) for i in range(6)]))

print(answer2([2, 7, 2, 4, 8, 1]))
print(answer([2, 7, 2, 4, 8, 1]))
# print(answer([1,1, 1, 7, 7, 7, 9, 18]))
print(answer2([1,3,3,6,6]))
# print(answer([1,3,3,6,6, 12]))
# print(answer([1,1,1, 1, 1, 6]))
# print(answer([1,1,1, 3, 6]))
print(answer2(range(1,7)))
# print(answer(range(1, 1000)))