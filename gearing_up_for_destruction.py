from fractions import Fraction

'''
given a list of peg locations, find radius of first gear s.t.
there as a gear on every peg, every gear touches, and the first gear is twice the radius of the last
output: [a,b] representing radius of the first gear, representing a/b (in lowest terms)
 '''

def answer(pegs):
    dist = list()
    for i in range(1, len(pegs)):
        dist.append(pegs[i] - pegs[i - 1])

    print(dist)
    r = 0
    mult = 1
    for d in reversed(dist):
        r += mult * d
        mult *= -1

    r2 = r
    if mult == -1:
        r2 *= Fraction(2, 3)
    else:
        r2 *= -2
    if r2 < 1:
        return [-1, -1]

    # check all the gears are positive radius
    r_next = r2
    print(r_next)
    for d in dist:
        r_next = d - r_next
        print(r_next)
        if r_next < 1:
            return [-1, -1]
    if mult == 1:
        r *= -2
        return [r, 1]
    r *= 2
    if r % 3 == 0:

        return [int(r/3), 1]
    else:
        return [r, 3]
        # your code here

# p = [4, 30, 50]
p = [5, 244]
# p = [12, 30, 60, 84, 94]
print(p)
print(answer(p))