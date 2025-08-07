import math
age=15
taille=1.74

base=int(input("entrer la base du triangle"))
hauteur=int(input("entrer la hauteur du triangle"))
print("la zone du triangle est de",0.5*base*hauteur)
cot1=int(input("entrer le 1er côté"))
cot2=int(input("entrer le 2ème côté"))
cot3=int(input("entrer le 3ème côté"))
print("le périmètre du triangle est ",cot1+cot2+cot3)
longueur=float(input("la longueur du rectangle"))
largeur=float(input("la largeur du rectangle"))
surface=longueur * largeur
perimetre=2*(longueur+largeur)
r=float(input("le rayon du cercle"))
zone=3.14*r**2
c=2*3.14*r
print("la surface",surface)
print("périmètre",perimetre)
print("zone",zone)
print('circonférence',c)
print("le point(2.2)")
x=float(input("la valeur de x"))
y=2*x-2
print("la valeur de y",y)
x1,y1=2,2
x2,y2=6,10
pente=((y2-y1) / (x2-x1))
print("la pente",pente)
distance=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print("la distance",distance)
print("je ne sais de quel comparaison ils parlent ")
def equation(x):
    return x**2+6*x+9
for x in range(-5,11):
    y=equation(x)
    if(y==0):
        print("la valeur de x est :",x)
print("la longueur de python est",len('python'),"celui de dragon est :",len('dragon'))
print(len('python')!=len('dragon'))
print("on" in "python" and "on" in "dragon")
phrase = "I hope this course is not full of jargon."
print("jargon" in phrase)
print("on" not in "python" and "on" not in "dragon")
text = "python"
long = len(text)
print("Longueur :", long)
print("Float :", float(long))
print("String :", str(long))

def paire(x):
    if(x%2==0):
        print(x," est divisible par 2")
    else:
        print(x,"n'est pas divisible par 2")
a=int(input("donne la valeur à vérifier si il est divisible par "))
paire(a)
print("vérification de  division de 7 par 3 " ,7/3 !=int(2.7) )
print(type(10)==type(10))
print(int(9.8)==10)
heure=int(input("Entrez les heures"))
taux=int(input("ENtrez le taux par heure "))
print("votre gain hebdomadaire est de:",heure*taux)
annee=int(input("entrez lz nbre d'années que vous voulez vivre"))
print("Vous vivrez pendant",annee*3600*365)
for i in range(3):
    for y in range (11):
        print('*', end=' ')
    print("")







