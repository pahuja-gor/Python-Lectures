import random
from string import ascii_lowercase


class Cipher:

    def __init__(self):
        self.__cipherText = ""
        self.__plainText = ""

    def getCipherText(self):
        return self.__cipherText

    def getPlainText(self):
        return self.__plainText

    def setCipherText(self, newCT):
        self.__cipherText = newCT

    def setPlainText(self, newPT):
        self.__plainText = newPT


class TranspositionCipher(Cipher):

    def __init__(self):
        pass

    def transpositionEncrypt(self):
        evenChars = ""
        oddChars = ""
        charCount = 0
        for ch in super().getPlainText():
            if charCount % 2 == 0:
                evenChars += ch
            else:
                oddChars += ch
            charCount += 1
        super().setCipherText(oddChars + evenChars)

    def transpositionDecrypt(self):
        cipherText = super().getCipherText()
        halfLength = len(cipherText) // 2  # len(x) = 20; halfLength = 10
        evenChars = cipherText[halfLength:]  # 10-19
        oddChars = cipherText[:halfLength]  # 0-9
        plainText = ""
        for i in range(halfLength):
            plainText += evenChars[i]
            plainText += oddChars[i]
        if len(oddChars) < len(evenChars):
            plainText += evenChars[-1]
        super().setPlainText(plainText)


class SubstitutionCipher(Cipher):

    def __init__(self):
        self.__key = ""

    def setKey(self, newKey):
        self.__key = newKey

    def keyGen(self):
        alphabet = ascii_lowercase + ' '
        key = ""
        for i in range(len(alphabet) - 1, -1, -1):
            index = random.randint(0, i)
            key = key + alphabet[index]
            alphabet = self.removeChar(alphabet, index)
        return key

    def removeChar(self, string, index):
        return string[:index] + string[index + 1:]

    def substitutionEncrypt(self):
        key = self.__key
        alphabet = ascii_lowercase + ' '
        plainText = super().getPlainText().lower()
        cipherText = ""
        for ch in plainText:
            index = alphabet.find(ch)
            cipherText += key[index]
        super().setCipherText(cipherText)

    def substitutionDecrypt(self):
        key = self.__key
        alphabet = ascii_lowercase + ' '
        plainText = ""
        for ch in super().getCipherText():
            index = key.find(ch)
            plainText += alphabet[index]
        super().setPlainText(plainText)

    def removeDupes(self, mystr):
        newstr = ""
        for ch in mystr:
            if ch not in newstr:
                newstr += ch
        return newstr

    def removeMatches(self, mystr, removeString):
        newstr = ""
        for ch in mystr:
            if ch not in removeString:
                newstr += ch
        return newstr

    def genKeyFromPass(self, password):
        alphabet = ascii_lowercase + ' '
        password = password.lower()
        password = self.removeDupes(password)
        lastChar = password[-1]
        lastIndex = alphabet.find(lastChar)
        afterString = self.removeMatches(alphabet[lastIndex + 1:], password)
        beforeString = self.removeMatches(alphabet[:lastIndex], password)
        key = password + afterString + beforeString
        self.__key = key

    def generateFromPassword(self):
        password = input("OK, I'll need a password: ")
        self.genKeyFromPass(password)

    def automatedKey(self):
        key = self.keyGen()
        print("Don't forget, your key is", key)
        self.__key = key


class VigenereCipher(Cipher):

    def __init__(self):
        pass

    def letterToIndex(self, letter):
        alphabet = ascii_lowercase + ' '
        index = alphabet.find(letter)
        return index

    def indexToLetter(self, index):
        alphabet = ascii_lowercase + ' '
        letter = alphabet[index]
        return letter

    def vigenereIndex(self, keyLetter, plainTextCharacter):
        keyIndex = self.letterToIndex(keyLetter)
        plainTextIndex = self.letterToIndex(plainTextCharacter)
        newIndex = (plainTextIndex + keyIndex) % 26
        return self.indexToLetter(newIndex)

    def encryptVigenere(self, key):
        cipherText = ""
        plainText = super().getPlainText()
        keyLen = len(key)
        for i in range(len(plainText)):
            ch = plainText[i]
            if ch == " ":
                cipherText += ch
            else:
                cipherText += self.vigenereIndex(key[i % keyLen], ch)
        super().setCipherText(cipherText)

    def undoVigenere(self, keyLetter, cipherTextCharacter):
        keyIndex = self.letterToIndex(keyLetter)
        cipherTextIndex = self.letterToIndex(cipherTextCharacter)
        newIndex = (cipherTextIndex - keyIndex) % 26
        return self.indexToLetter(newIndex)

    def decryptVigenere(self, key):
        cipherText = super().getCipherText()
        plainText = ""
        keyLen = len(key)
        for i in range(len(cipherText)):
            ch = cipherText[i]
            if ch == " ":
                plainText += ch
            else:
                plainText += self.undoVigenere(key[i % keyLen], ch)
        super().setPlainText(plainText)


def printSelectionMenu():
    print("Welcome to the super fancy encryption system!")
    print("")
    print("Pick your encryption algorithm of choice:")
    print("    1. Transposition Cipher")
    print("    2. Substitution Cipher")
    print("    3. Vigenere Cipher")
    print("")
    return choiceLimiter(["1", "2", "3"])


def printEncryptDecryptMenu():
    print("Will you be encrypting or decrypting today?")
    print("    1. Encrypt")
    print("    2. Decrypt")
    print("")
    return choiceLimiter(["1", "2"])


def getMessageToEncrypt():
    return input("Enter a message to encrypt: ")


def getMessageToDecrypt():
    return input("Enter a message to decrypt: ")


def printKeyStyleMenu():
    print("Do you want to enter your own key, or have one generated for you?")
    print("    1. Enter a key")
    print("    2. Make me a key")
    return choiceLimiter(["1", "2"])


def choiceLimiter(options):
    choice = 0
    while choice not in options:
        choice = input("Enter your selection: ")
    return int(choice)


def handleTransposition(encDec):
    tpObj = TranspositionCipher()

    if encDec == 1:
        text = getMessageToEncrypt()
        tpObj.setPlainText(text)
        tpObj.transpositionEncrypt()
        print("Encrypted:", tpObj.getCipherText())
    else:
        text = getMessageToDecrypt()
        tpObj.setCipherText(text)
        tpObj.transpositionDecrypt()
        print("Decrypted:", tpObj.getPlainText())


def handleSubstitution(encDec):
    sbObj = SubstitutionCipher()

    if encDec == 1:
        keyType = printKeyStyleMenu()
        # if keyType == 1:
        #     password = input("OK, I'll need a password: ")
        #     key = genKeyFromPass(password)
        # else:
        #     key = keyGen()
        #     print("Don't forget, your key is", key)

        keyTypeSwitcher = {
            1: sbObj.generateFromPassword,
            2: sbObj.automatedKey
        }

        keyTypeSwitcher[keyType]()

        text = getMessageToEncrypt()
        sbObj.setPlainText(text)
        sbObj.substitutionEncrypt()
        print("Encrypted:", sbObj.getCipherText())

    else:
        key = input("Sure, I'll need your key then: ")
        sbObj.setKey(key)

        if (len(key) != 27):
            sbObj.genKeyFromPass(key)

        text = getMessageToDecrypt()
        sbObj.setCipherText(text)
        sbObj.substitutionDecrypt()
        print("Decrypted:", sbObj.getPlainText())


def handleVigenere(encDec):
    vgObj = VigenereCipher()

    if encDec == 1:
        text = getMessageToEncrypt()
        vgObj.setPlainText(text)
        key = input("You'll need to enter a key: ")
        vgObj.encryptVigenere(key)
        print("Encrypted:", vgObj.getCipherText())

    else:
        text = getMessageToDecrypt()
        vgObj.setCipherText(text)
        key = input("Sure, I'll need your key then: ")
        vgObj.decryptVigenere(key)
        print("Decrypted:", vgObj.getPlainText())


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
        1: handleTransposition,
        2: handleSubstitution,
        3: handleVigenere
    }

    encryptionSwitcher[algorithm](encDec)


if __name__ == "__main__":
    main()