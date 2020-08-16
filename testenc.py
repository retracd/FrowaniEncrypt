#FrowaniEncrpyt v1.3.1
#Programmed fully by Brent Mayes. Original Creation.

#defines an encrypting function that translates letters to numbers and shifts the numbers down by twenty
def encrypt(sentence):

    result = []

    for letter in sentence:
        l = ((((ord(letter) - 20) * 7) / 2) - 63) * 2
        result.append(int(l))

    print("\nYour encrypted message is:\n")
    for numbers in result:
        print(numbers, end='')
        print(" ", end='')
    print(' ')
    again()

#defines a decrypting function that changes the string input to a list, which then adds twenty to each interger in the list, finally translating the numbers to letters
def decrypt(result):

    end_string = ""

    resultinterger = result.split()
    mapresult = map(int, resultinterger)
    resultlist = list(mapresult)

    for numbers in resultlist:
        l = int(numbers)
        l = int(((((l / 2) + 63) * 2) / 7) + 20)
        l = chr(l)
        end_string = end_string + l

    print("Your decrypted message is:\n")
    print(end_string)
    again()

#defines a function that asks whether you would like to encrypt or decrypt
def start():
    ende = input('\nWould you like to encrypt or decrypt? EN/DE: ')
    if ende == 'en' or ende == 'EN':
        enc = input('\nWhat would you like to encrypt:\n')
        encrypt(enc)
    if ende == 'de' or ende == 'DE':
        dec = input('\nWhat would you like to decrypt:\n')
        decrypt(dec)

#defines a function that asks if the user would like to encrypt/decrypt again
def again():
    translateagain = input('\nWould you like to encrypt/decrypt again? Y/N: ')
    if translateagain == "Y" or translateagain == 'y':
        start()
    elif translateagain == "N" or translateagain == 'n':
        print("Thank you for choosing FrowaniEncrpyt (v1.3.1)")
        quit()

#defines a function that is only called when the script is first run
def firststart():
    print("Starting FrowaniEncrpyt (v1.3.1)")
    start()

#since all of the above code is defining functions, this calls the function defined as start(), which of course starts the whole script
firststart()
