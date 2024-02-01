
def somme(x=0,y=0):
    return x+y

def produit(x=0,y=0):
    return x*y

def calcul(x=0,y=0):
    s=x+y
    p=x*y
    return s,p

class Point :
    def __init__(self, nom="", x=0, y=0):
        self.nom = nom
        self.x = x
        self.y = y
    def afficher(self):
        print("%s(%d,%d)"%(self.nom, self.x, self.y))
    def decaler(self, dx=0, dy=0):
        self.x += dx # self.x = self.x + dx
        self.y += dy # self.y = self.y + dy