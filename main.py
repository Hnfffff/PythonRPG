# This is the RPG text adventure game I am making instead of studying for trials
from sys import exit
from random import randrange
from sty import bg, fg
from os import system

import ItemClasses
import Levels
import Objects
import EnemyHolder

class Player:
    def __init__(self, name, healthBase, strengthBase, speedBase, faithBase, level):
        self.__name = str(name)

        # Main Stats
        self.__health = healthBase
        self.__strength = strengthBase
        self.__speed = speedBase
        self.__faith = faithBase
        self.__level = level

        self.__inventory = []
        self.__equipment = []

        self.__healthMod = 0
        self.__strengthMod = 0
        self.__speedMod = 0
        self.__faithMod = 0

        self.__xpos = 0
        self.__ypos = 0

        self.__oldPos = " "

        self.__currentScene = ""

    def GetX(self):
        return self.__xpos

    def GetY(self):
        return self.__ypos

    def GetPosition(self):
        print(f"X: {self.__xpos}, Y: {self.__ypos}")

    def SetX(self, newvalue):
        self.__xpos = newvalue

    def SetY(self, newvalue):
        self.__ypos = newvalue

    def GetScene(self):
        return self.__currentScene

    def ChangeLevel(self, scene, sceneholder):
        self.__xpos = 0
        self.__ypos = 0
        sceneholder.clear()
        match scene:
            case "Dungeon1":
                for i in Levels.Dungeon1:
                    sceneholder.append(i)
                    self.__currentScene = scene
                self.SetPosition(23, 23)

            case "WaterRoom":
                for i in Levels.WaterRoom:
                    sceneholder.append(i)
                    self.__currentScene = scene
                self.SetPosition(5, 7)

            case "GrassField":
                for i in Levels.GrassField:
                    sceneholder.append(i)
                    self.__currentScene = scene
                self.SetPosition(5, 6)

            case "ErrorRoom":
                for i in Levels.ErrorLevel:
                    sceneholder.append(i)
                    self.__currentScene = scene
                self.SetPosition(5, 7)

    def Collision(self):
        match Levels.Scene[self.__ypos - 1][self.__xpos - 1]:
            case "|" | "-" | "+" | "#":
                print("Cant move in that Direction")
                return False

            case "~":
                Levels.itemcolor["0"] = fg(20) + bg(26)
                return True

            case "T":
                print("The Trees are too thick to walk through!")
                return False

            case "=":
                choice = input("This will take you to a different area. Proceed? (y/n): ")
                if choice == "y":
                    temp = "ErrorRoom"
                    for i in Objects.Doors:
                        print(i.GetIdentifier())
                        print(f"{self.__xpos}{self.__ypos}{self.__currentScene}")
                        if i.GetIdentifier() == f"{self.__xpos}{self.__ypos}{self.__currentScene}":
                            temp = i.GetWarpPoint()
                    self.__currentScene = temp
                    self.ChangeLevel(temp, Levels.Scene)
                    return "LevelChange"
                else:
                    print("Chose not to proceed")
                    system('cls')
                    return False

            case _:
                Levels.itemcolor["0"] = fg(20)
                return True

    def MoveLeft(self):
        Levels.Scene[self.__ypos - 1][self.__xpos - 1] = self.__oldPos
        self.__xpos -= 1

        match self.Collision():
            case False:
                self.__xpos += 1
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"

            case True:
                self.SetOldPos()
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
                system('cls')

            case _:
                print("Swapped Levels")

    def MoveRight(self):
        Levels.Scene[self.__ypos - 1][self.__xpos - 1] = self.__oldPos
        self.__xpos += 1

        match self.Collision():
            case False:
                self.__xpos -= 1
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
            case True:
                self.SetOldPos()
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
                system('cls')
            case _:
                print("Swapped Levels")

    def MoveUp(self):
        Levels.Scene[self.__ypos - 1][self.__xpos - 1] = self.__oldPos
        self.__ypos -= 1

        match self.Collision():
            case False:
                self.__ypos += 1
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
            case True:
                self.SetOldPos()
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
                system('cls')
            case _:
                print("Swapped Level")

    def MoveDown(self):
        Levels.Scene[self.__ypos - 1][self.__xpos - 1] = self.__oldPos
        self.__ypos += 1

        match self.Collision():
            case False:
                self.__ypos -= 1
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
            case True:
                self.SetOldPos()
                Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"
                system('cls')
            case _:
                print("Swapped Level")

    def SetPosition(self, x, y):
        # self.SetOldPos()
        self.__ypos = y
        self.__xpos = x
        self.SetOldPos()
        Levels.Scene[self.__ypos - 1][self.__xpos - 1] = "0"

    def SetOldPos(self):
        self.__oldPos = Levels.Scene[self.__ypos - 1][self.__xpos - 1]

    def GetName(self):
        return self.__name

    def GetLevel(self):
        return self.__level

    def Equip(self):
        index = int(input("> Index of item to equip?: "))
        try:
            self.__equipment.append(self.__inventory[index - 1])
            self.SetStats()
        except:
            print("Error, Index out of Range!")

    def ShowInventory(self):
        if len(self.__inventory) >= 1:
            for i in self.__inventory:
                x = 1
                print(f">{x}: {i.GetItemName()}: GearScore: {i.GetGearScore()}")
        else:
            print("Empty!")

    def AddInventory(self, item):
        self.__inventory.append(item)

    def RemoveInventory(self):
        index = int(input("> Index of item to Remove?: ")) - 1
        try:
            confirm = input(
                f"Are you sure you would like to Destroy {self.__inventory[index].GetItemName()}: GearScore: {self.__inventory[index].GetGearScore()}? (y/n)").lower()
            if confirm == "y":
                self.__inventory.pop(index)
                print("Successfully Removed Item!")
            else:
                print("Aborted Destruction!")
        except:
            print("Error, Index of of Range!")

    def SetStats(self):
        self.__healthMod = 0
        self.__strengthMod = 0
        self.__speedMod = 0
        self.__faithMod = 0

        for i in self.__equipment:
            if self.__equipment[self.__equipment.index(i)] is not None:
                self.__healthMod = self.__equipment[self.__equipment.index(i)].GetHealthMod()
                self.__strengthMod = self.__equipment[self.__equipment.index(i)].GetStrengthMod()
                self.__speedMod = self.__equipment[self.__equipment.index(i)].GetSpeedMod()
                self.__faithMod = self.__equipment[self.__equipment.index(i)].GetFaithMod()

    def ShowStats(self):
        print(f""">Name: {self.__name} -=- Level: {self.__level}
Strength: {self.__strength + self.__strengthMod} (Base {self.__strength} + {self.__strengthMod})
Health: {self.__health + self.__healthMod} (Base {self.__health} + {self.__healthMod})
Speed: {self.__speed + self.__speedMod} (Base {self.__speed} + {self.__speedMod})
Faith: {self.__faith + self.__faithMod} (Base {self.__faith} + {self.__faithMod})""")


def ShowMap(holder):
    for i in holder:
        temp = ""
        for j in i:
            temp += Levels.itemcolor[j] + " " + j + " " + fg.rs + bg.rs
        print(temp)




player = Player("james", 10, randrange(1, 5), randrange(1, 5), randrange(1, 5), 1)


player.ChangeLevel("GrassField", Levels.Scene)

funcdictionary = {"stats": player.ShowStats, "removeitem": player.RemoveInventory, "inventory": player.ShowInventory,
                  "equip": player.Equip, "exit": exit, "moveright": player.MoveRight, "moveleft": player.MoveLeft,
                  "moveup": player.MoveUp, "movedown": player.MoveDown, "position": player.GetPosition}

if __name__ == "__main__":
    EnemyHolder.testenemy.SetPosition(8, 9)
    player.AddInventory(ItemClasses.Shield("Iron Shield", 5, 0, -5, 0, player.GetLevel()))
    while True:
        for j in EnemyHolder.enemies:
            if j.Getlevel() == player.GetScene():
                #ShowMap(Levels.Scene)
                j.Move(randrange(-1,1), randrange(-1,1), randrange(1,2))
        ShowMap(Levels.Scene)
        choice = str(input(fg(40) + "> "))
        try:
            if choice.lower() == "map":
                system('cls')
            else:
                funcdictionary[choice]()
        except SystemExit:
            exit()
        except:
            print("Error")
