def reverseString(text: str):
    n = len(text)
    text = list(text)
    special_characters = list("!@#$%^&*()-+?_=,<>/")
    #print(special_characters)

    i = 0
    j = n-1
    while i < j:
        if text[i] not in special_characters:
            print(True)
            tmp = text[i]
            text[i] = text[j]
            text[j] = tmp
        else:
            print(False)
            print(text[i])

        i += 1
        j -= 1
    print(text)



print(reverseString("a,b$cd"))