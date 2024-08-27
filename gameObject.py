from pygame import Surface
class transform():
    def __init__(self, x:int,y:int,z:int):
        self.x = x
        self.y = y
        self.z = z
    def setPos(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z
    def getPos(self) -> tuple:
        t = (self.x, self.y, self.z)
        return t
    def movePos(self, x:int, y:int):
        self.x += x
        self.y += y

class gameObject:
    def __init__(self, name:str, transform:transform):
        self.name = name
        self.transform = transform
        self.surf = None
    def draw(self):
        x = int(self.transform.getPos()[0]+Surface.get_width(self.surf)/2)
        y = int(self.transform.getPos()[1]+Surface.get_height(self.surf)/2)
        self.surf.set_at((x, y), (255, 255, 255))
    def update(self):
        self.transform.movePos(1,0)
