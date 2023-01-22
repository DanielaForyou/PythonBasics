# EXERCITII OBLIGATORII
# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# varibila- valoare alocată unei zone de memorie

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
import math
job = 'Profesor'
ani = 16
media = 8.634578
diploma_in_domeniu = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(job))
print(type(ani))
print(type(media))
print(type(diploma_in_domeniu))
print('-------------------------------')

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
media=round(media)
print(media)
print(type(media))
print('--------------------------------')

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Sunt {job} cu {ani} in domeniu.')
print(f'Media studentei care vrea sa paraseasca facultatea este {media}.')
print(f'Document care atesta calificarea in domeniu: {diploma_in_domeniu}')
print(f'De {ani} ani ma exprim prin muzica.')
print('---------------------------------')

'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
numele=input('Numele: ')
prenumele=input('Prenumele: ')
print(f'Numele complet are {len(numele)+len(prenumele)} caractere')
print('---------------------------------')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
lungimea=int(input('Introduceti lungimea dreptunghiului: '))
latimea=int(input('Introduceti latimea dreptunghiului: '))
aria=lungimea*latimea
print(f'Aria dreptunghiului este {aria}')
print('--------------------------------')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''
coral='Coral is either the stupidest animal or the smartest rock'
print(coral.count(' the '))
#daca scriu fara spatiu 'the' imi va numara 3 din cauza cuvantului 'either'
# trebuie sa pun spatii daca vreau anume cuvantul, nu doar combinatia de litere
print('---------------------------------')

# 10. Același string.
#   ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
#assert coral.isdigit()
# https://pythonguides.com/python-find-number-in-string/


# EXERCITII OPTIONALE

'''
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
string_impar= input('Scrieti un string de dimensiune impara: ')
caracter=string_impar[math.floor(len(string_impar)/2)]
print(f'Caracterul din mijloc este: {caracter}')
print('----------------------------------')

# 2. Folosind assert, verifică dacă un string este palindrom.
# assert string_impar[:]==string_impar[::-1]

'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
a,b=input('Scrie numele si prenumele: ').split()
print(a)
print(b)
print('-----------------------------------')

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
test=input('Scrie un string: ')
primul_caracter=test[0]
last_index=len(test)-1
print(f'{test[0:1]}{test[1:last_index].replace(primul_caracter,primul_caracter.upper())}{test[-1]}')
print('------------------------------------')

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''
user=input('User: ')
parola=input('Parola: ')
x='*'*len(parola)
print(f'Parola pentru user {user} este {x} si are {len(parola)} caractere')
print('------------------------------------')
















