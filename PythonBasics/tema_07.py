#Exerciții obligatorii - grad de dificultate: Usor spre Mediu
'''
1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
acum la ore.
Curs git/github https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
'''


'''
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI=3.14

    @abstractmethod
    def Aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''
class Patrat(FormaGeometrica):
    __latura=0
    def __init__(self,latura):
        self.__latura=latura
    @property
    def latura(self):
        return self.latura

    @latura.getter
    def latura(self):
        print(f'Latura patratului este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self,latura):
        self.__latura = latura
        print(f'Noua lungime a laturii este {latura}')

    @latura.deleter
    def latura(self):
        print('Am sters lungimea laturii')
        self.__latura=0

    def Aria(self):
        aria=self.__latura**2
        print(f'Aria patratului este {aria}')

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''
class Cerc(FormaGeometrica):
    __raza=0
    def __init__(self,raza):
        self.raza=raza
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este{self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self,raza):
        self.__raza=raza
        print(f'Noua raza este {raza}')

    @raza.deleter
    def raza(self):
        self.__raza=0
        print('Am sters lunigimea razei')

    def Aria(self):
        aria=self.PI*self.__raza**2
        print(f'Aria cercului este {aria}')

    def descrie(self):
        print('Eu nu am colturi')
'''
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''
patrat1=Patrat(3)
patrat1.latura
del patrat1.latura
patrat1.latura=4
patrat1.latura
patrat1.Aria()

print('-----cerc-----')

cerc1=Cerc(3)
cerc1.descrie()
cerc1.Aria()
del cerc1.raza
cerc1.raza=6
cerc1.Aria()
'''
3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public
Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
'''