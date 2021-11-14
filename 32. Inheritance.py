from Classes_Objects import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()


"""
1. Stworzyłem klase Chef w pliku Classes_Objects
2. Zaimportowałem
3. Przypisałem ją do myChef - od teraz myChef ma te funkcje co Chef
4. Stworzyłem nowy plik ChineseChef
5. Zinheritowałem, zdziedziczyłem funkcje klasy Chef do klasy ChineseChef
6. Nadpisałem jedną z funkcji Chef w ChineseChef
"""
