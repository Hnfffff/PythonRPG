import Levels
from sty import fg, bg

class BaseEnemy:
    def __init__(self, name, icon, sceneholder, damage, health, scene):
        self.damage = damage
        self.health = health
        self.name = name
        self.icon = icon
        self.sceneholder = sceneholder
        self.scene = scene

        self.__xpos = 0
        self.__ypos = 0

        self.oldpos = ""

    def Getlevel(self):
        return self.scene
    def GetIcon(self):
        return self.icon
    def SetOldPos(self):
        self.oldpos = self.sceneholder[self.__ypos - 1][self.__xpos - 1]

    def ChangePosition(self, x, y):
        self.__xpos = x
        self.__ypos = y
        self.sceneholder[self.__ypos - 1][self.__xpos-1] = self.icon

    def SetPosition(self,x,y):
        self.__ypos = y
        self.__xpos = x
        self.SetOldPos()
        self.sceneholder[self.__ypos - 1][self.__xpos - 1] = self.icon

    def CollisionCheck(self):
        match Levels.Scene[self.__ypos - 1][self.__xpos - 1]:
            case "|" | "-" | "+" | "#" | "=":
                print("EnemyCollision Detected")
                return False

            case "~":
                Levels.itemcolor["0"] = fg(20) + bg(26)
                return True

            case "T":
                print("EnemyCollision Detected")
                return False

            case _:
                return True

    #def ChooseDirection

    def Move(self, directionx, directiony, absolutedirection):
        self.sceneholder[self.__ypos-1][self.__xpos-1] = self.oldpos

        #main.ShowMap(self.sceneholder)
        match absolutedirection:
            case 1:
                match directionx:
                    case -1:
                        self.__xpos -= 1
                        match self.CollisionCheck():
                            case True:
                                self.SetPosition(self.__xpos, self.__ypos)
                            case False:
                                self.__xpos +=1
                                self.ChangePosition(self.__xpos, self.__ypos)
                    case 1:
                        self.__xpos += 1
                        match self.CollisionCheck():
                            case True:
                                self.SetPosition(self.__xpos, self.__ypos)
                            case False:
                                self.__xpos -= 1
                                self.ChangePosition(self.__xpos, self.__ypos)
                            case _:
                                print("SOMETHINGS WRIONG!!!")
                    case _:
                        self.ChangePosition(self.__xpos,self.__ypos)
            case 2:
                match directiony:
                    case -1:
                        self.__ypos -= 1
                        match self.CollisionCheck():
                            case True:
                                self.SetPosition(self.__xpos,self.__ypos)
                            case False:
                                self.__ypos +=1
                                self.ChangePosition(self.__xpos, self.__ypos)
                    case 1:
                        self.__ypos += 1
                        match self.CollisionCheck():
                            case True:
                                self.SetPosition(self.__xpos,self.__ypos)
                            case False:
                                self.__ypos -= 1
                                self.ChangePosition(self.__xpos, self.__ypos)
                    case _:
                        self.ChangePosition(self.__xpos, self.__ypos)



