# importer le module calcul
import calcul

# Appeler la fonction somme définie dans le module calcul
print(calcul.somme(10,20))

# Appeler la fonction calcul définie dans le module calcul
s,p=calcul.calcul(10,20)
print("{0:d}+{1:d}={2:d} , {0:d}*{1:d}={3:d}".format(10,20,s,p))

# Créer un objet de type Point
p=calcul.Point("P1",2,3)
p.afficher()
p.decaler(dy=2,dx=4)
p.afficher()