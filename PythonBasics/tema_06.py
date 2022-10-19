'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

class Cerc:
    # fields (atribuite)
    raza=None
    culoare=None

    #constructor
    def __init__(self,raza,culoare):
        self.raza=raza
        self.culoare=culoare

    # metode
    def descriere_cerc(self):
        print(self.raza,self.culoare)
    def aria (self):
        aria=3.14*self.raza**2
        print(aria)
    def diametru(self):
        diametru=self.raza*2
        print(diametru)
    def circumferinta(self):
        c=2*3.14*self.raza
        print(c)


'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''

class Dreptunghi:
    lungime=0
    latime=0
    culoare=None

    def __init__(self,lungime,latime,culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare

    def descriere(self):
        print(self.lungime,self.latime,self.culoare)

    def aria(self):
        aria=self.latime*self.lungime
        print(aria)
    def perimetrul(self):
        p=2*(self.lungime+self.latime)
        print(p)
    def schimba_culoarea(self,noua_culoare):
        self.culoare=noua_culoare

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
class Angajat:
    nume=None
    prenume=None
    salariu=0

    def __init__(self,nume,prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu=salariu

    def descriere(self):
        print(self.nume,self.prenume,self.salariu)
    def nume_complet(self):
        print(self.nume,self.prenume)
    def salariu_lunar(self ):
        print(self.salariu)
    def salariu_anual(self):
        print(self.salariu*12)
    def marire_salariu(self,procent):
        m=self.salariu+(self.salariu/100*procent)
        print(m)


'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
class Cont:
    iban=None
    titular_cont=None
    sold=0

    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self,suma):
        if suma<=self.sold:
            self.sold-=suma
            print(f'Soldul dupa debitare este: {self.sold}')
        else:
            print('Nu aveti sufcienti bani in cont')
    def creditare_cont(self,suma):
        self.sold+=suma
        print(f'Soldul dupa creditare este: {self.sold}')

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
'''
from datetime import date
date.today()
class Factura:
    seria='01102022'
    numar=None
    nume_produs=None
    cantitate=0
    pret_buc=0

    def __init__(self,numar,nume_produs,cantitate,pret_buc):
        self.numar=numar
        self.nume_produs=nume_produs
        self.cantitate=cantitate
        self.pret_buc=pret_buc

    def schimba_cantitatea(self,cantitate):
        self.cantitate=cantitate
    def schimba_pretul(self,pretul):
        self.pret_buc=pretul
    def schimba_nume_produs(self,nume):
        self.nume_produs=nume
    def genereaza_factura(self):
        total=self.pret_buc*self.cantitate
        print(f'''Factura seria {self.seria} numar {self.numar}
Data: {date.today()}
Produs: {self.nume_produs} |Cantitate: {self.cantitate} |Pret bucata: {self.pret_buc} |Total: {total}
Telefon | 7 | 700 | 49000''')

print('---------Clasa Factura--------')
apa=Factura(1,"apa",10,30,)
apa.genereaza_factura()




'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''
class Masina:
    marca='BMW'
    model=None
    viteza_maxima=0
    viteza_actuala=0
    culoare='gri'
    culori_disponibile=['negru','alb','rosu','indigo','violet']
    inmatriculata=False

    def __init__(self,model,viteza_maxima):
        self.model=model
        self.viteza_maxima=viteza_maxima

    def descriere(self):
        print(f'Marca {self.marca}, '
              f'model {self.model},'
              f'viteza_maxima {self.viteza_maxima},'
              f'viteza_actuala {self.viteza_actuala},'
              f'culoare {self.culoare},'
              f'inmatriculata {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata=True
    def vopseste(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare=culoare
        else:
            print('Culoarea nu este disponibila')
    def accelereaza(self,viteza):
        if viteza>=0:
            self.viteza_actuala += viteza
            if self.viteza_actuala>self.viteza_maxima:
                self.viteza_actuala=self.viteza_maxima
        else:
            print('Viteza negativa - eroare')
    def franeaza(self):
        self.viteza_actuala=0

masina1=Masina('xs',180)
print('------------CLASA MASINA ------------')

'''
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''
class TodoList():
    todo={}
    def adauga_task(self,nume,descriere):
        self.todo.update({nume:descriere})
    def finalizeaza_task(self,nume):
        self.todo.pop(nume)
    def afiseaza_todo_list(self):
        print(self.todo.keys())
    def afiseaza_detalii_suplimentare(self,nume_task):
        if not nume_task in self.todo.keys():
            raspuns=input('Acest task nu e in todo list. Doriti sa il adaugati? ("da" sau "nu"): ')
            if raspuns=='da':
                nume=input('Introduceti numele task-ului: ')
                descriere=input('Introduceti descrierea: ')
                self.todo.update({nume:descriere})
            else:
                print('La revedere')
        else:
            print(self.todo[nume_task])

print('-------Clasa TodoList--------')
todolist=TodoList()
