# EXERCITII OBLIGATORII

'''1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# print(masini)
# x=input('Introduceti marca masinii preferate: ')
#
# for i in range (0,len(masini)):
#     if i==masini.index(x):
#         print(f'Masina mea preferata este {x}')
#
# for masina in masini:
#     if masina==x:
#         print(f'Masina mea preferata este {x}')
#
# i=0
# while i<len(masini):
#     i+=1
#     if i==masini.index(x):
#         print(f'Masina mea preferata este {x}')

'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
#
# for i in range (1,len(masini)-1):
#     masini[i]=masini[i].upper()
# else:
#     print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Nu am găsit mașina X. Mai căutam‘
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# print(masini)
# x=input('Itroduceti marca masinei dorite: ')
# for masina in masini:
#     if masina==x:
#         print('Am gasit masina dorita de dvs')
#         break
# else:
#     print(f'Nu am gasit masina {x}. Mai cautam')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina=='Lastun' or masina=='Trabant':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
# masini_vechi=[]
# for masina in masini:
#     if masina=='Lastun' or masina=='Trabant':
#         masini_vechi.append(masina)
#         masini[masini.index(masina)]='Tesla'
# print(f'Modelele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă. 
'''
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
#
# masini=[]
# for masina in pret_masini.items():
#     if masina[1]<= 15000:
#         masini.append(masina[0])
# print(masini)
#
# for masina in masini:
#     print(f'Pentru un buget de sub 15000 euro puteți alege mașina {masina}')

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x=0
# for numar in numere:
#     if numar==3:
#         x+=1
# print(f'Numarul 3 apare de {x} ori')

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma=0
# for i in range(0,len(numere)):
#     suma+=numere[i]
# print(suma)

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x=0
# for numar in numere:
#     if numar>x:
#         x=numar
# print(x)

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
# numere_negative=[]
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for numar in numere:
#     if numar>0:
#         numere_negative.append(-numar)
#     else:
#         numere_negative.append(numar)
# print(numere_negative)

# EXERCITII OPTIONALE

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar>0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#     if numar%2==0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
# print(f'Numere pozitive: {numere_pozitive}')
# print(f'Numere negative: {numere_negative}')
# print(f'Numere pare: {numere_pare}')
# print(f'Numere impare: {numere_impare}')

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for j in range(len(alte_numere)):
#     for i in range(len(alte_numere)-j-1):
#         if alte_numere[i] > alte_numere[i + 1]:
#             alte_numere[i], alte_numere[i + 1] = alte_numere[i + 1], alte_numere[i]
# print(alte_numere)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
# import random
# numar_secret=random.randint(1,30)
# numar_ghicit=None
# while numar_ghicit!=numar_secret:
#     numar_ghicit = int(input('Alege un nr intre 1 si 30: '))
#     numar_secret = random.randint(1, 31)
#     if numar_ghicit>numar_secret:
#         print(numar_secret)
#         print('Nr secret e mai mic')
#     elif numar_secret>numar_ghicit:
#         print(numar_secret)
#         print('Nr secret e mai mare')
# print(numar_secret)
# print('Felicitari! Ai ghicit!')

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
'''
# x=int(input('Alegeti un numar:'))
# for i in range(1,x+1):
#     print(str(i)*i)
'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# for i in range(len(tastatura_telefon)):
#     for numar in tastatura_telefon[i]:
#         print(f'Numarul curent este {numar}')
