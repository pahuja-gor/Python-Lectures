import random
from string import ascii_lowercase

def printSelectionMenu():
    print("Welcome to the super fancy encryption system!")
    print("")
    print("Pick your encryption algorithm of choice:")
    print("    1. Transposition Cipher")
    print("    2. Substitution Cipher")
    print("    3. Vigenere Cipher")
    print("")
    return choiceLimiter(["1","2","3"])

def printEncryptDecryptMenu():
    print("Will you be encrypting or decrypting today?")
    print("    1. Encrypt")
    print("    2. Decrypt")
    print("")
    return choiceLimiter(["1","2"])

def getMessageToEncrypt():
    return input("Enter a message to encrypt: ")

def getMessageToDecrypt():
    return input("Enter a message to decrypt: ")

def printKeyStyleMenu():
    print("Do you want to enter your own key, or have one generated for you?")
    print("    1. Enter a key")
    print("    2. Make me a key")
    return choiceLimiter(["1","2"])

def choiceLimiter(options):
    choice = 0
    while choice not in options:
        choice = input("Enter your selection: ")
    return int(choice)



# Transposition functions follow

def transpositionEncrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars += ch
        else:
            oddChars += ch
        charCount += 1
    cipherText = oddChars + evenChars
    return cipherText

def transpositionDecrypt(cipherText):
    halfLength = len(cipherText) // 2   # len(x) = 20; halfLength = 10
    evenChars = cipherText[halfLength:] # 10-19
    oddChars = cipherText[:halfLength]  # 0-9
    plainText = ""
    for i in range(halfLength):
        plainText += evenChars[i]
        plainText += oddChars[i]
    if len(oddChars) < len(evenChars):
        plainText += evenChars[-1]
    return plainText
    


# Substitution functions follow

def keyGen():
    alphabet = ascii_lowercase + ' '
    key = ""
    for i in range(len(alphabet)-1, -1, -1):
        index = random.randint(0, i)
        key = key + alphabet[index]
        alphabet = removeChar(alphabet, index)
    return key

def removeChar(string, index):
    return string[:index] + string[index+1:]

def substitutionEncrypt(plainText, key):
    alphabet = ascii_lowercase + ' '
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        index = alphabet.find(ch)
        cipherText += key[index]
    return cipherText

def substitutionDecrypt(cipherText, key):
    alphabet = ascii_lowercase + ' '
    plainText = ""
    for ch in cipherText:
        index = key.find(ch)
        plainText += alphabet[index]
    return plainText

def removeDupes(mystr):
    newstr = ""
    for ch in mystr:
        if ch not in newstr:
            newstr += ch
    return newstr

def removeMatches(mystr, removeString):
    newstr = ""
    for ch in mystr:
        if ch not in removeString:
            newstr += ch
    return newstr

def genKeyFromPass(password):
    alphabet = ascii_lowercase + ' '
    password = password.lower()
    password = removeDupes(password)
    lastChar = password[-1]
    lastIndex = alphabet.find(lastChar)
    afterString = removeMatches(alphabet[lastIndex+1:], password)
    beforeString = removeMatches(alphabet[:lastIndex], password)
    key = password + afterString + beforeString
    return key



# Vigenere functions follow

def letterToIndex(letter):
    alphabet = ascii_lowercase + ' '
    index = alphabet.find(letter)
    return index

def indexToLetter(index):
    alphabet = ascii_lowercase + ' '
    letter = alphabet[index]
    return letter

def vigenereIndex(keyLetter, plainTextCharacter):
    keyIndex = letterToIndex(keyLetter)
    plainTextIndex = letterToIndex(plainTextCharacter)
    newIndex = (plainTextIndex + keyIndex) % 26
    return indexToLetter(newIndex)

def encryptVigenere(plainText, key):
    cipherText = ""
    keyLen = len(key)
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == " ":
            cipherText += ch
        else:
            cipherText += vigenereIndex(key[i % keyLen], ch)
    return cipherText

def undoVigenere(keyLetter, cipherTextCharacter):
    keyIndex = letterToIndex(keyLetter)
    cipherTextIndex = letterToIndex(cipherTextCharacter)
    newIndex = (cipherTextIndex - keyIndex) % 26
    return indexToLetter(newIndex)

def decryptVigenere(cipherText, key):
    plainText = ""
    keyLen = len(key)
    for i in range(len(cipherText)):
        ch = cipherText[i]
        if ch == " ":
            plainText += ch
        else:
            plainText += undoVigenere(key[i % keyLen], ch)
    return plainText



# Encryption Managers

def handleTransposition(encDec):
    if encDec == 1:
        text = getMessageToEncrypt()
        print("Encrypted:", transpositionEncrypt(text))
    else:
        text = getMessageToDecrypt()
        print("Decrypted:", transpositionDecrypt(text))

def generateFromPassowrd():
    password = input("OK, I'll need a password: ")
    key = genKeyFromPass(password)
    return key

def automatedKey():
    key = keyGen()
    print("Don't forget, your key is", key)
    return key

def handleSubstitution(encDec):
    if encDec == 1:
        keyType = printKeyStyleMenu()
        # if keyType == 1:
        #     password = input("OK, I'll need a password: ")
        #     key = genKeyFromPass(password)
        # else:
        #     key = keyGen()
        #     print("Don't forget, your key is", key)

        keyTypeSwitcher = {
            1 : generateFromPassowrd,
            2 : automatedKey
        }

        key = keyTypeSwitcher[keyType]()

        text = getMessageToEncrypt()
        print("Encrypted:", substitutionEncrypt(text, key))
        
    else:
        key = input("Sure, I'll need your key then: ")
        
        if (len(key) != 27):
            key = genKeyFromPass(key)
        
        text = getMessageToDecrypt()
        print("Decrypted:", substitutionDecrypt(text, key))

def handleVigenere(encDec):
    if encDec == 1:
        text = getMessageToEncrypt()
        key = input("You'll need to enter a key: ")
        print("Encrypted:", encryptVigenere(text, key))
        
    else:
        text = getMessageToDecrypt()
        key = input("Sure, I'll need your key then: ")
        print("Decrypted:", encryptVigenere(text, key))


def main():
    algorithm = printSelectionMenu()
    encDec = printEncryptDecryptMenu()
    
    # if algorithm == 1:
    #     handleTransposition(encDec)
    # elif algorithm == 2:
    #     handleSubstitution(encDec)
    # else:
    #     handleVigenere(encDec)
    
    encryptionSwitcher = {
        1 : handleTransposition,
        2 : handleSubstitution,
        3 : handleVigenere
    }

    encryptionSwitcher[algorithm](encDec)

if __name__ == "__main__":
    main()