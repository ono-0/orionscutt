plaintext = input("enter plaintext")
plaintextlength = len(plaintext)
listplace = 0
plaintextlist = list(plaintext)
print(plaintextlist)
while plaintextlength != listplace:
    ciphertext = chr(ord(plaintextlist[listplace]) + 1)
    print(ciphertext)
    listplace = listplace + 1