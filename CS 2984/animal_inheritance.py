class Animal:
    def __init__(self, iName, iAge, iLocation):
        self.__name = iName
        self.__age = iAge
        self.__favoriteLocation = iLocation

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getLocation(self):
        return self.__favoriteLocation

    def setName(self, newName):
        self.__name = newName

    def setAge(self, newAge):
        self.__age = newAge

    def setLocation(self, newLocation):
        self.__favoriteLocation = newLocation

    def speak(self):
        print("The animal is speaking")


class Cat(Animal):
    def __init__(self, iName, iAge, iLocation, iLength):
        self.__whiskerLength = iLength
        super().__init__(iName, iAge, iLocation)

    def meow(self):
        print("Meow!")

    def speak(self):
        # print("MEOW!")
        super().speak()


class Dog(Animal):
    def __init__(self, iName, iAge, iLocation):
        super().__init__(iName, iAge, iLocation)
        self.__numberOfTailWags = 0

    def fetch(self):
        print("The dog is now playing fetch")

    def wag(self):
        self.__numberOfTailWags += 1

    def getNumberOfTailWags(self):
        return self.__numberOfTailWags

    def speak(self):
        print("BARK!")


fluffy = Cat("Fluffy", 7, "windows", 3)
fluffy.meow()
print(fluffy.getName())
fluffy.setName("FLUFFY")
print(fluffy.getName())

print('----------')

fido = Dog("Fido", 3, "outside")
fido.fetch()
print(fido.getName())
fido.setName("FIDO")
print(fido.getName())
for x in range(10):
    fido.wag()
print(fido.getNumberOfTailWags())

print('----------')

mysteryAnimal = Animal("?????", 123, "Mars")
print(mysteryAnimal.getName())

print('----------')

fluffy.speak()
fido.speak()
mysteryAnimal.speak()
