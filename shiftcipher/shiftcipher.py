#importing fuctions
from shiftcipherdecrypt import abcdecrypt
from shiftcipherencrypt import abcencrypt
#giving user choice between which fuction to run
choice = int(input("Choose to encrypt or decrypt.\nEnter 1 to encrypt.\nEnter 2 to decrypt."))
if choice == 1:
    abcencrypt()
elif choice == 2:
    abcdecrypt()
else:
    print("ERROR")