from random import randrange

class Equipable:
    def __init__(self, itemName, healthMod, strengthMod, speedMod, faithMod, playerLevel):
        self.__itemName = str(itemName)
        self.__healthMod = healthMod
        self.__strengthMod = strengthMod
        self.__speedMod = speedMod
        self.__faithmod = faithMod
        self.__gearscore = randrange(1, playerLevel + 1)
        self.__itemTag = ""

    def GetItemName(self):
        return self.__itemName

    def GetHealthMod(self):
        return self.__healthMod

    def GetStrengthMod(self):
        return self.__strengthMod

    def GetSpeedMod(self):
        return self.__speedMod

    def GetFaithMod(self):
        return self.__faithmod

    def GetGearScore(self):
        return self.__gearscore

    def GetItemTag(self):
        return self.__itemTag

class Shield(Equipable):
    def __init__(self, itemName, healthMod, strengthMod, speedMod, faithMod, playerLevel):
        super().__init__(itemName, healthMod, strengthMod, speedMod, faithMod, playerLevel)
        self.__itemTag = "Shield"


