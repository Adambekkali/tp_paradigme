#EXO1
from functools import reduce


prix_euros = [50, 20, 35, 100, 80]
taux_conversion = 1.10
prix_dollars = list(map(lambda prix: prix * taux_conversion, prix_euros))
prix_dollars_symbole = list(map(lambda prix: f"{prix:.2f}$", prix_dollars))

print("Exercice 1 :")
print("Prix en dollars :", prix_dollars_symbole)


#EXO2

ages=[12, 25, 17, 18, 40, 15, 22]

adultes = list(filter(lambda age: age >= 18, ages))
print("Exo 2 \n Adultes :",adultes)


#Exo 3

ventes=[120, 50, 30, 20, 90, 100]

total_ventes = reduce(lambda x, y: x + y, ventes)

# Produit des ventes
produit_ventes = reduce(lambda x, y: x * y, ventes)

print("\nExercice 3 :")
print("Total des ventes :", total_ventes)
print("Produit des ventes :", produit_ventes)




# Exercice 4 : Combinaison de map, filter et reduce

notes = [12, 15, 9, 18, 6, 20, 14]


notes_sur_100 = list(map(lambda note: note * 5, notes))

notes_sup_50 = list(filter(lambda note: note >= 50, notes_sur_100))

moyenne = reduce(lambda x, y: x + y, notes_sup_50) / len(notes_sup_50) if notes_sup_50 else 0

print("\nExercice 4 :")
print("Notes sur 100 :", notes_sur_100)
print("Notes ≥ 50 :", notes_sup_50)
print("Moyenne des notes ≥ 50 :", moyenne)


#Exo 5