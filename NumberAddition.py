
def NumberAddition(string):

    nu = "1234567890"
    res = " "
    i = 0
    n = 0
    while i < len(string):
        if string[i] in nu:
            res += string[i]
            n += 1
        if string[i] not in nu:
            if res[n] != "." and n != 0 and i != len(string)-1:
                res += "."
                n += 1
        i += 1

    res = res.replace(" ", "")
    res = res.split(".")

    r = 0
    i = 0
    while i < len(res):
        if res[i] != "":

            r += int(res[i])
        i += 1
    return r

print NumberAddition(raw_input())
