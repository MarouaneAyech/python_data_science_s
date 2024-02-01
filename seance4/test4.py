# A partir de module calcul, importer somme et produit en leus donnant des alias (shortnames)
from calcul import somme as s, produit as p

# Appeler la fonction somme définie dans le module calcul
print(s(10,20))

# Appeler la fonction produit définie dans le module calcul
print(p(10,20))