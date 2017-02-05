# map a->z, b-> y, etc in a string

def answer(s):
    code = 'abcdefghijklmnopqrstuvwxyz'
    trans = {code[i]: code[-(i+1)] for i in range(len(code))}
    ls = list(s)
    for i, c in enumerate(s):
        if c in trans:
            ls[i] = trans[c]
    return "".join(ls)

print(answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
