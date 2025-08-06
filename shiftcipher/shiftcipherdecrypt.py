#creating function
def abcdecrypt():
    #getting user inputs
    ciphertext = input("enter ciphertext")
    key = int(input("enter key"))
    #setting variables
    ciphertextlength = len(ciphertext)
    plaintext = ""
    listplace = 0
    #spliting ciphertext
    ciphertextlist = list(ciphertext)
    while ciphertextlength != listplace:
        #the actual cipher
        plaintextpart = chr(ord(ciphertextlist[listplace]) + -key)
        #moving while function
        plaintext = plaintext + plaintextpart
        listplace = listplace + 1
    #printing plaintext result
    print(plaintext)