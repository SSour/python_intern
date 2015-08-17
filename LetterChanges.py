def LetterChanges(str):

    vov = ['a', 'e', 'i', 'o', 'u']

    str = str.replace("z", "a")
    str = str.replace("y", "z")
    str = str.replace("x", "y")
    str = str.replace("w", "x")
    str = str.replace("v", "w")
    str = str.replace("u", "v")
    str = str.replace("t", "u")
    str = str.replace("s", "t")
    str = str.replace("r", "s")
    str = str.replace("q", "r")
    str = str.replace("p", "q")
    str = str.replace("o", "p")
    str = str.replace("n", "o")
    str = str.replace("m", "n")
    str = str.replace("l", "m")
    str = str.replace("k", "l")
    str = str.replace("j", "k")
    str = str.replace("i", "j")
    str = str.replace("h", "i")
    str = str.replace("g", "h")
    str = str.replace("f", "g")
    str = str.replace("e", "f")
    str = str.replace("d", "e")
    str = str.replace("c", "d")
    str = str.replace("b", "c")
    str = str.replace("a", "b")

    i = 0
    while i < len(str):
        if str[i] in vov:
            str = str.replace(str[i], str[i].upper())
        i += 1
    return str

print LetterChanges(raw_input()) 
