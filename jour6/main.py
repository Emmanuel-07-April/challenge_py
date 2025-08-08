a=()
s=('ama','afi','rose')
g=('kodjo','kossi')
c=s+g
family_Menbers=c+('Maman','Père',)
print(c)
print(len(c))
print(family_Menbers)
fr=family_Menbers[0:3]
soeur=family_Menbers[3:5]
parent=family_Menbers[5:7]
print(fr)
print(soeur)
print(parent)
Fruits = ('banane', 'orange', 'mango', 'citron')
legumes = ("carotte", "brocoli", "poivron", "courgette", "chou-fleur")
produits_animaux = (
    "lait",
    "œufs",
    "miel",
    "fromage",
    "viande de bœuf",
    "jambon",
    "yaourt",
    "crème",
    "beurre",
    "poisson"
)
food_stuff_tp= Fruits+legumes+produits_animaux
print(food_stuff_tp)
food_stuff_LT= list(food_stuff_tp)
print(food_stuff_LT)
milieu= len(food_stuff_LT)
print(milieu)
premiers=food_stuff_LT[:3]
derniers=food_stuff_LT[-3:]
del(food_stuff_tp)
nordic_countries = ("Estonie", "Islande", "Norvège", "Suède", "Finlande", "Danemark")
print("Estonie" in nordic_countries)  # True
print("Iceland" in nordic_countries)


