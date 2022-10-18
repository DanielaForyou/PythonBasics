# EXERCITII OBLIGATORII

# # 1.Funcție care să calculeze și să returneze suma a două numere
# def suma(x,y):
#     suma=x+y
#     return suma
# print(suma(2,3))

# # 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def numa_par(x):
#     if x%2==0:
#         par=True
#     else:
#         par=False
#     return par
# print(numa_par(6))

# # 3. Funcție care returnează numărul total de caractere din numele tău complet.
# # (nume, prenume, nume_mijlociu)
# def nr_caractere(nume,prenume,nume_mijlociu=('')):
#     caractere=len(nume)+len(prenume)+len(nume_mijlociu)
#     return caractere
# print(nr_caractere('Foiu','Daniela'))


# # 4. Funcție care returnează aria dreptunghiului
# def aria_dreptunghiului(x,y):
#     aria=x*y
#     return aria
# print(aria_dreptunghiului(3,4))

# # 5. Funcție care returnează aria cercului
# def aria_cercului(r):
#     aria=3.14*r*r
#     return aria
# print(aria_cercului(2))

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
'''
# def gaseste_string():
#     prop=input('Introduceti un string: ')
#     x=input('Introduceti caracterul cautat: ')
#     if x in prop:
#         caracter_x=True
#     else:
#         caracter_x=False
#         return caracter_x
# print(gaseste_string())
#
'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
# def lower_upper():
#     prop=input('Introduceti stringul: ')
#     x=('')
#     y=('')
#     for i in range (len(prop)):
#         if prop[i]==prop[i].lower():
#             x+=prop[i]
#         else:
#             y+=prop[i]
#     print(f'Nr de caractere lower case este {len(x)}')
#     print(f'Nr de caractere upper case este {len(y)}')
# lower_upper()

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
# def numere_pozitive(*args):
#     lista=[]
#     lista+=args
#     pozitive=[]
#     for i in lista:
#         if i>=0:
#             pozitive.append(i)
#     return pozitive
# print(numere_pozitive(1,2,-3,-6,0,400))

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
# def comparare(x,y):
#     if x>y:
#         print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif y>x:
#         print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#     else:
#         print('Numerele sunt egale.')
#
# comparare(7,6)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
# def add_numere_set(x,set):
#     if not(x in set):
#         set.add(x)
#         print('Am adaugat numarul nou in set')
#         return True
#     else:
#         print('Nu am adaugat numarul in set. Acesta exista deja.')
#         return False
#
# print(add_numere_set(2,{1,2,3,4}))


# EXERCITII OPTIONALE

# # 1. Funcție care primește o lună din an și returnează câte zile are acea luna
# def zile_in_luna(luna):
#     zile_31=['ianuarie','martie','mai','iulie','august','octombire','decembrie']
#     zile_30=['aprilie','iunie','septembrie','noiembrie']
#     zile_28=['februarie']
#     luni=zile_28+zile_31+zile_30
#     if luna in luni:
#         if luna in zile_31:
#             return (f'{luna} are 31 de zile')
#         elif luna in zile_30:
#             return (f'{luna} are 30 de zile')
#         else:
#             return (f'{luna} are 28 de zile')
#     print('Nu exista ')
#
# print(zile_in_luna('martie'))


'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''
# def calculator(x,y):
#     a=x+y
#     b=x-y
#     c=x*y
#     d=x/y
#     return a,b,c,d
#
# a,b,c,d=calculator(7,4)
# print('Suma:',a)
# print('Diferenta:',b)
# print('Inmultirea:',c)
# print('Impartirea:',d)


'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
# def lista_de_cifre(lista=[]):
#
#     dictionar={
#         0:lista.count(0),
#         1:lista.count(1),
#         2:lista.count(2),
#         3:lista.count(3),
#         4:lista.count(4),
#         5:lista.count(5),
#         6:lista.count(6),
#         7:lista.count(7),
#         8:lista.count(8),
#         9:lista.count(9),
#     }
#     return dictionar
#
# print(lista_de_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5]))


#4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

# def valoarea_maxima(x,y,z):
#     if x>=y and x>=z:
#         return x
#     elif y>=x and y>=z:
#         return y
#     else:
#         return z
#
# print(valoarea_maxima(1,4,4))


'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
# def suma_nr(x):
#     suma_nr=0
#     for i in range(x+1):
#         suma_nr+=i
#     return suma_nr
#
# print(suma_nr(3))

# EXERCITII OPTIONALE - Bonus

'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

# def numere_comune(list1=[],list2=[]):
#     numere_comune=[]
#     for i in list1 and list2:
#         if i in list1 and list2:
#             if numere_comune.count(i)==0:
#                 numere_comune.append(i)
#     return numere_comune
#
# print(numere_comune([1,1,2,3],[2,2,3,4]))


'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''

# def reducere(pret,reducere):
#     if reducere<0 or reducere>100:
#         return ('Reducere invalida')
#     else:
#         pret_redus=pret-(pret/100*reducere)
#         return pret_redus
#
# print(reducere(100,10))

'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''

#NU STIU

'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''
#  NU STIU
