import Levels
class Door:
    def __init__(self, icon, warppoint, name, x, y):
        self.__icon = icon
        self.__warpPoint = warppoint
        self.__x = x
        self.__y = y

        self.__name = name

    def GetSpawnX(self):
        return self.__spawnx

    def GetSpawnY(self):
        return self.__spawnx

    def GetIcon(self):
        return self.__icon

    def GetWarpPoint(self):
        return self.__warpPoint

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def GetName(self):
        return self.__name

    def GetIdentifier(self):
        return f"{self.__x}{self.__y}{self.__name}"

    def SetPosition(self,x,y, level):
        level[y-1].pop(x-1)
        level[y-1].insert(x-1, self.__icon)


WaterRoomDungeon1 = Door("=", "Dungeon1", "WaterRoom", 5,8)
WaterRoomDungeon1.SetPosition(5,8, Levels.WaterRoom)
Dungeon1WaterRoom = Door("=", "WaterRoom", "Dungeon1", 19, 1)
Dungeon1WaterRoom.SetPosition(19,1,Levels.Dungeon1)
Dungeon1GrassField = Door("=", "Dungeon1", "GrassField", 5, 5)
Dungeon1GrassField.SetPosition(5,5,Levels.GrassField)
GrassFieldDungeon1 = Door("=", "GrassField", "Dungeon1", 23, 24)
GrassFieldDungeon1.SetPosition(23,24,Levels.Dungeon1)



Doors = [Dungeon1WaterRoom, Dungeon1GrassField, WaterRoomDungeon1, GrassFieldDungeon1]
