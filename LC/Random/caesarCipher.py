def cipher(text: str, shift: int):
    print("Original Text: {}".format(text))
    print("Shifted by: {}".format(shift))

    text = list(text)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alphabet)

    for i in range(len(text)):
        character = text[i]
        text[i] = alphabet[(alphabet.index(character)+shift)%n]
    
    return ''.join(text)

print(cipher("ATTACKATONCE", 4))