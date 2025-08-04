f = open("ciphertextdatabase.log", "a")
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
with open("ciphertextdatabase.log", "a") as f:
    f.write(ciphertext)
    f.write("\n")
print("test")