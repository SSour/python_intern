def FirstReverse(str): 

    text = ""
    l = len(str)-1
    while l != -1:
        text += str[l]

        l -= 1
    return text

print FirstReverse(raw_input()) 
