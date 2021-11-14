from Classes_Objects import Chef


class ChineseChef(Chef):  # wystarczy wpisać zaimportowaną klase Chef w () by klasa ChineseChef odziedziczyła jej funkcję

    def make_special_dish(self):  # nadpisanie dziedziczonej funkcji make_special_dish, PyCharm pokazuje ikonke po lewej nawet
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        self.is_not_used()  # ad1. Kasuje błąd o static
        print("Chef makes fried rice")

    def is_not_used(self):  # ad1. Kasuje błąd o static
        pass
