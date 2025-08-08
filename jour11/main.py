import math
from collections import Counter
from itertools import count


def add_two_numbers(n1,n2):
    return n1+n2
def area_of_circle(r):
    return 3.14*r**2
def add_all_nums(*nbre):
    s=0
    for i in nbre:
        if (type(i)==int):
             s+=i
        else:
            print("impossible de faire la somme d'un",type(i))
    return s
def convert_celsius_to_fahrenheit(deg):
    return (deg*(9/5))+32
def Check_Season(mois):
    if(mois.lower() in ('mars','avril','mai')):
        return 'printemps'
    elif(mois.lower() in ('juin','juillet','août')):
        return 'Ete'
    elif(mois.lower() in ('septembre','octobre','novembre')):
        return 'automne'
    else:
        return 'hiver'
def calculate_slope(x1,x2,y1,y2):
        if ((x2-x1)==0):
            return 'vérifier le x1 et x2'
        return (y2-y1)/(x2-x1)
def solve_quadratic_eqn(a,b,c,):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return "Pas de solution réelle"
def print_list(a):
    for i in a :
        print(i,end=' ')
def Reverse_list(a):
     a.reverse()
     return  a
def CAPITalizelist_items(a):
     for i in range(len(a)):
         a[i]=a[i].upper()
     return a
def add_item(a,b):
    a.append(b)
    return a
def Remove_item(a,b):
    a.remove(b)
    return a
def SUM_OF_NUMBERS(a):
    s=0
    for i in range(1,a+1):
        s=s+i
    return s
def SUM_OF_ODDS(a):
    s=0
    for i in range(1,a+1):
        if (i%2!=0):
            s=s+i
    return s
def SUM_OF_EVEN(a):
    s=0
    for i in range(1,a+1):
        if (i%2==0):
            s=s+i
    return s
def evens_and_odds(a):
    s=0
    t=0
    for i in range(0,a+1):
        if (i%2==0):
            s=s+1
    print("paire",s)
    for i in range(0, a + 1):
        if (i % 2 != 0):
            t = t + 1
    print("impair",t)
def factoriel(a):
    s=1
    for i in range (1,a+1):
        s=s*i
    return s
def is_empty(a):
    if (a==''):
        print('vide')
    else:
        print('no vide')
def calculer_mean(a):
    return sum(a) / len(a)
def median(a):
    b=sorted(a)
    c=len(b)
    med=c//2
    if c%2==0:
        return (b[med-1]+b[med])/2
    else:
        return b[med]
def calculer_mode(a):
    s=Counter(a)
    print(s)
    g=max(s.values())
    for i in range(len(a)):
        if(a.count(i)==g):
            return i
def calculer_range(a):
     return max(a)-min(a)
def calculer_variance(a):
    n=len(a)
    s=0
    for i in range(n):
        s=s+i
    moy =s/n
    p=0
    for i in range(n):
        p=p+(i-moy)**2
    vari=(1/n)*p
    return p
def calculer_std(a):
    return math.sqrt(calculer_variance(a))
def IS_PRIME(a):
        if a < 2:
            return  a," n'est pas premier"
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return a," n'est pas premier"
        return a," est premier"
def verifiez(a):
    return len(a)==len(set(a))
def mm_type(a):
    b=type(a[0])
    return all(type(i)==b for i in a)
def valide(a):
    return a.isidentifier()
def plus_pose():
    return "anglais,francais,allemand,espagnol"





print(add_two_numbers(1,3))
print(area_of_circle(3))
print(add_all_nums(2,5,'a',4,8,4))
print(convert_celsius_to_fahrenheit(12.5))
print(Check_Season('JANVIER'))
print(calculate_slope(2, 3, 4, 7))
print(solve_quadratic_eqn(1, -3, 2))
a=['15','d',5,5805,5]
print(print_list(a))
print(Reverse_list(a))
b=["e",'e','fgf']
print(CAPITalizelist_items(b))
print(add_item(a,'ok'))
print(add_item(b,'cool'))
print(Remove_item(a,'ok'))
print(SUM_OF_NUMBERS(5))
print(SUM_OF_ODDS(5))
print(SUM_OF_EVEN(5))
print(evens_and_odds(100))
print(factoriel(5))
print(is_empty(1))
c=[1,2,5,2,5,3,6,8,9,2]
print(calculer_mode(c))
print(calculer_range(c))
donnees = [2, 4, 6, 8, 10]
print(calculer_variance(donnees))
print(calculer_std(donnees))
print(IS_PRIME(121))
print(verifiez(c))
print(mm_type(a))
print(valide(('2dik')))






