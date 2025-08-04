def abcdecrypt():
    ciphertext = input("enter ciphertext")
    key = int(input("enter key"))
    ciphertextlength = len(ciphertext)
    plaintext = ""
    listplace = 0
    ciphertextlist = list(ciphertext)
    while ciphertextlength != listplace:
        plaintextpart = chr(ord(ciphertextlist[listplace]) + -key)
        plaintext = plaintext + plaintextpart
        listplace = listplace + 1
    print(plaintext)