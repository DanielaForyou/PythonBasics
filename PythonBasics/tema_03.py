# EXERCITII OBLIGATORII
'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''

'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''
note_muzicale=['do','re','mi','fa','sol','la','si','do']
print(f'Lista initiala este: {note_muzicale}')
note_muzicale=note_muzicale[::-1]
print(f'Lista dupa suprascriere prin slicing este: {note_muzicale}')
note_muzicale.reverse()
print(f'Lista dupa metoda reverse este: {note_muzicale}')
print('---------------------------')

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))
print('---------------------------')

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lista_1=[3,1,0,2]
lista_2=[6,5,4]
# lista_1.append(lista_2) # adauga lista_2 ca element nou in lista_1
# print(lista_1)
# lista_3=lista_1,lista_2 # ambele liste devin elemente in lista_3
# print(lista_3)
# print('-----------------------------')
lista_4=lista_1+lista_2 # se unesc intr-o singura lista
print(lista_4)
lista_1.extend(lista_2) # se unesc intr-o singura lista
print(lista_1)
print('---------------------------')

'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
print(f'Lista dupa unirea elementelor este: {lista_1}')
lista_1.sort()
print(f'Lista dupa sortare este: {lista_1}')
lista_1.remove(0)
print(f'Lista dupa ce a fost extras elementul 0 este: {lista_1}') # nu am inteles cum sa sortez un numar
print('----------------------------')

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
'''
if lista_1==[]:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')
print('---------------------------')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista_1.clear()
print(lista_1)
print('--------------------------')

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if lista_1==[]:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')
print('---------------------------')

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
print('---------------------------')

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print(f'Ana a luat nota {dict1.get("Ana")}') # trebuie sa pun apostroafe diferite pentru a nu fi confundate cu cele de formatare
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')
print('-----------------------------')

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
dict1.update({'Dorel':6})
print(f'Dupa contestatie Dorel a luat nota {dict1["Dorel"]}')
print('-----------------------------')

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
dict1.pop('Gigel')
print(f'Gigel s-a transferat din clasa')
dict1['Ionica']=9
print(f'Vine un nou coleg. Noii elevi sunt {dict1.keys()}')
print('---------------------------')

'''
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni') # un set nu poate avea dublicate
print(zile_sapt)
print('------------------------')

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')
print('---------------------------')

# 14. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt.difference(weekend))
print('---------------------------')

# 15. Afișază intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))
print('---------------------------')

# EXERCITII OPTIONALE

'''
 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
Google search hint
“how to check if item îs în list python”
 '''
jucatori=['Marin','Ion','Andrei','Vasile','Mihai']
print(jucatori)
list(jucatori)
schimbari=0

while schimbari<3:
    jucator_scos = input('Itroduceti numele jucatorului scos: ')
    if jucator_scos in jucatori:
        schimbari += 1
        jucator_intrat = input('Introduceti numele jucatorului intrat: ')
        jucatori.remove(jucator_scos)
        jucatori.append(jucator_intrat)
        print(f'A intra {jucator_intrat}, a ieșit {jucator_scos}, mai ai {3 - schimbari} schimbări')
        print(jucatori)
        print('----------------------')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_scos} nu e în teren')
        print(f'Mai ai {3 - schimbari} schimbari')
        print(jucatori)
        print('----------------------')
print('Nu mai poti face schimbari. Ai efectuat 3.')





