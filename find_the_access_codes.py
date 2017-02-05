import random

# MISREAD QUESTION KMS
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

def answer3(l):
    col, row = [], []
    for i in range(1, len(l)):
        col.append(sum([1 if (l[i] % l[q] == 0) else 0 for q in range(i)]))
        row.append(sum([1 if (l[q] % l[i] == 0) else 0 for q in range(i + 1, len(l))]))

    return sum([a * b for a, b in zip(col, row)])

def answer4(l):
    count = 0
    size = len(l)
    if size < 3: return 0

    cache = [0] * size
    for x in xrange(size):
        for y in xrange(x + 1, size):
            if l[y] % l[x] == 0:
                cache[y] += 1
                count += cache[x]

    return count

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


# def answer2(l):
#     tot=0
#     l2 = sorted(l)
#     dup = dict()
#     dup[l2[0]] = False
#     for i in range(1, len(l)):
#         if l2[i] in dup:
#             dup[l2[i]] = True
#         else:
#             dup[l2[i]] = False
#
#     n = len(dup)
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 d1 = (l2[j]+ 0.0)/l2[i]
#                 d2 = (l2[k]+0.0)/l2[j]
#                 if int(d1) == d1 and int(d2) == d2:
#                     tot+=1
#     return tot

def answer(l):
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
    if answer0(l) != answer4(l):
        print(l)
        print(answer0(l), answer4(l))
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