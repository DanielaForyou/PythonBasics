# if/else - operatie folosita atunci cand in dependetnta de conditii vrem sa rezolve problema diferit.
'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
 Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
 X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
 X este un int.
 '''

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# if/else - sistem logic de operare

x=int(input('Introduceti un nr x: '))

# 2. Verifică și afișează dacă x este număr natural sau nu.
if x>=0:
    print('x este nr natural')
else:
    print('x nu este nr natural')
print('----------------------------')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x>0:
    print('x este nr pozitiv')
elif x==0:
    print('x este nr neutru')
else:
    print('x este nr negativ')
print('----------------------------')

# 4. Verifică și afișează dacă x este între -2 și 13.
if -2<x<13:
    print('x este intre -2 si 13')
else:
    print('x nu este intre -2 si 13')
print('----------------------------')
# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x=int(input('Introduceti un nr x: '))
y=int(input('Introduceti un nr y:'))

if x-y<5:
    print('diferenta dintre x si y este mai mica de 5')
else:
    print('diferenta dintre x si y nu este mai mica de 5')
print('----------------------------')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not((x<27)and(x>5)):
    print('x NU este intre 5 si 27')
else:
    print('x este intre 5 si 27')
print('-----------------------------')

#  x și y (int)
# 7.Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
if x==y:
    print('x si y sunt egale')
elif x>y:
    print('x este mai mare ca y')
else:
    print('y este mai mare ca x')
print('------------------------------')

# x, y, z - laturile unui triunghi.
# 8.Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x=int(input('Introduceti prima latura a triunghiului: '))
y=int(input('Introduceti a 2-a latura a triunghiului: '))
z=int(input('Introduceti a 3-a latura a triunghiului: '))

if x<=0 or y<=0 or z<=0:
    print('Nu exista triunghi cu aceste laturi')
else:
    if x == y and y == z:
        print('Triunghiul este echilateral')
    elif x == y or x == z or y == z:
        print('Triunghiul este isoscel')
    else:
        print('E un triunghi oarecare')
print('--------------------------------')

#9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu.
litera=str(input('Introduceti o litera: '))

if litera=='a'or litera=='e'or litera=='i'or litera=='o'or litera=='u':
    print('Litera este o vocala')
else:
    print('Litera este o consoana')
print('----------------------------------')

'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
nota=float(input('Introduceti nota:'))
if nota>=9:
    print('A')
elif nota>=8:
    print('B')
elif nota>=7:
    print('C')
elif nota>=6:
    print('D')
elif nota>4:
    print('E')
else:
    print('F')
print('------------------------------------')

# EXERCITII OPTIONALE
#cum afla cate cifre sunt intr-un numar
import math
n=int(input('Introduceti un numar:'))
if n > 0:
    digits = int(math.log10(n))+1
elif n == 0:
    digits = 1
else:
    digits = int(math.log10(-n))+2  # +1 if you don't count the '-'
print(digits)
print('--------------------------')

#1.Verifică dacă x are minim 4 cifre (x e int).
#(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
if digits==4:
    print(f'{n} are 4 cifre')
elif digits>4:
    print(f'{n} are mai mult de 4 cifre')
else:
    print(f'{n} nu are minim 4 cifre')
print('------------------------------')

#2.Verifică dacă x are exact 6 cifre.
if digits==6:
    print(f'{n} are 6 cifre')
else:
    print(f'{n} nu are 6 cifre')
print('------------------------------')

#3.Verifică dacă x este număr par sau impar (x e int).
if n%2==0:
    print(f'{n} este un numar par')
else:
    print(f'{n} este un numar impar')
print('---------------------------------')

# x, y, z (int)
# 4.Afișează care este cel mai mare dintre ele?
x=int(input('Introduceti valoarea x: '))
y=int(input('Introduceti valoarea y: '))
z=int(input('Introduceti valoarea z: '))

if x>y and x>z:
    print(f'{x} este cel mai mare numar')
elif y>x and y>z:
    print(f'{y} este cel mai mare numar')
elif z>x and z>y:
    print(f'{z} este cel mai mare numar')
else:
    print('Cel mai mare numar nu a fost indentificat')
print('----------------------------------')

# x, y, z - reprezintă unghiurile unui triunghi
# 5.Verifică și afișează dacă triunghiul este valid sau nu.
x=int(input('Introduceti valoarea unghiului x: '))
y=int(input('Introduceti valoarea unghiului y: '))
z=int(input('Introduceti valoarea unghiului z: '))

if x+y+z==180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')
print('---------------------------------')

'''
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
prop=('Coral is either the stupidest animal or the smartest rock')
x=int(input('Introduceti un nr x:'))
print(prop[0:len(prop)-x])
print('----------------------------------')

#7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
string_nou=(prop[0:5]+prop[len(prop)-5:])
print(string_nou)
print('-----------------------------------')

'''
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
'''
rock=int(prop.index('rock'))
print(rock)
print(prop[0:rock])
print('----------------------------')

'''
9. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''

unString=str(input('Inrtoduceti un text: '))
prim_caracter=unString[0]
ultim_caracter=unString[-1]
assert prim_caracter.lower()or prim_caracter.upper()==ultim_caracter.upper() or ultim_caracter.lower(), "Primul si ultimul caracter nu sunt la fel"
print('----------------------------------')

'''
10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''
numere='0123456789' #slicing [start:end:step]
#afiseaza numerele pare
print(numere[2::2])
#afiseaza numerele impare
print(numere[1::2])
print('-------------------------')

# EXERCITII BONUS (MAY NEED GOOGLE)
'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''
x=int(input('Introdu un numar de la 1 la 6: '))
import random
y=random.randint(1,6)
if 0<x<=6:
    if x<y:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {y}')
    elif x>y:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {y}')
    else:
        print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {y}')
else:
    print('Numarul dumneavoastra nu corespunde cerintei')
print('---------------------------')

