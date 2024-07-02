class BaseEnemy:
    def __init__(self, name, icon, scene, damage, health):
        self.damage = damage
        self.health = health
        self.name = name
        self.icon = icon
        self.scene = scene

        self.__xpos = 0
        self.__ypos = 0

        self.oldpos = ""

    def GetIcon(self):
        return self.icon
    def SetOldPos(self):
        self.__oldPos = Scene[self.__ypos - 1][self.__xpos - 1]

    def SetPosition(self,x,y):
        self.__ypos = y
        self.__xpos = x
        self.SetOldPos()
        Scene[self.__ypos - 1][self.__xpos - 1] = "0"

    def Move(self, directionx, directiony):
        match directionx:
            case 1:
                self.__xpos -=1
                self.SetPosition(self.__xpos, self.__ypos)
            case 2:
                self.__xpos +=1
                self.SetPosition(self.__xpos)

        match directiony:
            case 1:
                self.__ypos -= 1
                self.SetPosition(self.__xpos,self.__ypos)
            case 2:
                self.__ypos -= 1
                self.SetPosition(self.__xpos,self.__ypos)




