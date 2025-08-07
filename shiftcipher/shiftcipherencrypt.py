#creating function
def abcencrypt():
    #getting user inputs
    plaintext = input("enter plaintext")
    key = int(input("enter key"))
    #setting variables
    plaintextlength = len(plaintext)
    ciphertext = ""
    listplace = 0
    #splitting plaintext
    plaintextlist = list(plaintext)
    while plaintextlength != listplace:
        #the actual cipher
        ciphertextpart = chr(ord(plaintextlist[listplace]) + key)
        #moving while function
        ciphertext = ciphertext + ciphertextpart
        listplace = listplace + 1
    #printing ciphertext result
    print(ciphertext)