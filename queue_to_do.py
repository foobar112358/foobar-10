def answer2(start, length):
    skip = length
    answer = 0
    for row in xrange(length):
        for val in xrange(length-row):
            answer ^= start
            start += 1
        start += (length-skip)
        skip -=1
    print answer

# 1^...^n
def xor_sum(n):
    ans = [n, 1, n+1, 0]
    return ans[n%4]

# a^(a+1)^...^b
def xor_range(a,b):
    return xor_sum(b)^xor_sum(a-1)

def answer(start, length):
    ans = 0
    for i in range(length):
        ans = ans^xor_range(start + i*length, start + length*(i+1)-i-1)
    print ans

#
# print(0^1^2)
# print(6^7^8)
# print(10^11^12^13^14)
answer (0,1)
answer (0,2)
answer (0,3)
answer (0,4)
answer(20000000,4)
# answer (0,5)
# answer (0,6)
# answer (0,7)
# answer (0,8)
# answer (0,9)
# answer(0,15)
# answer(1,32)
