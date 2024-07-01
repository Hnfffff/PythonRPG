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

WaterRoomDungeon1 = Door("=", "Dungeon1", "WaterRoom", 5,8)

Dungeon1WaterRoom = Door("=", "WaterRoom", "Dungeon1", 19, 1)

Dungeon1GrassField = Door("=", "Dungeon1", "GrassField", 5, 5)

GrassFieldDungeon1 = Door("=", "GrassField", "Dungeon1", 23, 24)



Doors = [Dungeon1WaterRoom, Dungeon1GrassField, WaterRoomDungeon1, GrassFieldDungeon1]
