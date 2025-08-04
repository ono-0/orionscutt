def abcencrypt():
    f = open("ciphertextdatabase.log", "a")
    plaintext = input("enter plaintext")
    key = int(input("enter key"))
    plaintextlength = len(plaintext)
    ciphertext = ""
    listplace = 0
    plaintextlist = list(plaintext)
    while plaintextlength != listplace:
        ciphertextpart = chr(ord(plaintextlist[listplace]) + key)
        ciphertext = ciphertext + ciphertextpart
        listplace = listplace + 1
    print(ciphertext)
    with open("ciphertextdatabase.log", "a") as f:
        f.write(ciphertext)
        f.write("\n")