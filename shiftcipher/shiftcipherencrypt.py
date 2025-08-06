#creating function
def abcencrypt():
    #opening/creating log file
    f = open("ciphertextdatabase.log", "a")
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
    #adding ciphertext to log file
    with open("ciphertextdatabase.log", "a") as f:
        f.write(ciphertext)
        f.write("\n")