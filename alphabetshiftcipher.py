plaintext = input("enter plaintext")
plaintextlength = len(plaintext)
ciphertext = ""
listplace = 0
plaintextlist = list(plaintext)
while plaintextlength != listplace:
    ciphertextpart = chr(ord(plaintextlist[listplace]) + 1)
    ciphertext = ciphertext + ciphertextpart
    listplace = listplace + 1
print(ciphertext)