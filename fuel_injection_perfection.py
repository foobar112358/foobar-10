def answer(n):
    tot = 0
    b = bin(int(n))[2:]
    while len(b) > 1:
        tot += 1
        if b[-1] == '0':
            b = b[:-1]
        elif b[-2] == '1':
            if b == '11':
                tot += 1
                b = '1'
            else:
                b = bin(int(b, base=2) + 1)[2:]
        else:
            b = bin(int(b, base=2) - 1)[2:]
    return tot



# print(bin(int('0'))[2:])
print(answer('3'))

# print(answer('123123123123123123133333332345353453453453453'))