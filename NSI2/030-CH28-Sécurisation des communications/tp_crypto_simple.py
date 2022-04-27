ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cesar(message: str, decode=False) -> str:
    offset = -3 if decode else 3
    result = ''
    for symbol in message:
        if symbol == ' ':
            letter = ' '
        else:
            letter = ALPHABET[(ALPHABET.index(symbol) + offset) % len(ALPHABET)]
        result += letter
    return result


def vigenere(message: str, key: str, decode=False) -> str:
    offset = -1 if decode else 1
    result = ''
    for i in range(len(message)):
        if message[i] == ' ':
            letter = ' '
        else:
            index_letter_message = ALPHABET.index(message[i])
            index_key_message = ALPHABET.index(key[i % len(key)])
            letter = ALPHABET[(index_letter_message + offset * index_key_message) % len(ALPHABET)]
        result += letter
    return result


crypted = vigenere("SALUT LA COMPAGNIE", "TROPCOOL")
print(crypted)
print(vigenere(crypted, "TROPCOOL", decode=True))
