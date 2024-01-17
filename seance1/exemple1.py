# variable de nom nom et de type str (chaine de caractères)
nom="Ali"
# variable de nom salaire et de type float (réel)
salaire=1200.7654
# variable de nom age et de type int (entier)
age=28
# avriable de nom celibataire et de type bool (booléen)
celibataire=True
# Afficher les informations
# On appelle la fonction print
print(nom)
print(salaire)
print(age)
print(celibataire)
# On affiche toutes les informations en une seule ligne
print("L'employé",nom,"a comme salaire",salaire,"et comme age",age,"celibataire=",celibataire)
# print possède des arguments optionnels : sep et end
print("L'employé",nom,"a comme salaire",salaire,"et comme age",age,"celibataire=",celibataire,
      sep='|', end=';')
print("hello")