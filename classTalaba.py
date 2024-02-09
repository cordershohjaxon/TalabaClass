class Talaba:
    """ Talana nomli class yaratamiz"""
    def __init__(self,ism,familya,tyil):
         """Talabaninfg xususiyatlari"""
         self.ism = ism
         self.familya = familya
         self.tyil = tyil
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    def get_lastname(self):
        """Talabaning familyasini qaytaradi"""
        return self.familya
    def get_full_name(self):
        """Talabaning to'liq ism,familyasini qaytaradi"""
        return f"{self.ism} {self.familya}"
    def birth_date(self):
        """Talabaning tug'ilgan yilini qaytaradi"""
        return self.tyil
    def get_age(self,yil):
        """Talabaning yoshini qaytaruvchi funksiya"""
        return yil-self.tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familya}.{self.tyil} da tug'ilganman")

talaba = Talaba("Alijon","Valiyev",2000)
talaba2 =Talaba("Husan","Akbarov",2004)
talaba3 =Talaba("Hasan","Akbarov",2004)

print(talaba.get_full_name())
talaba3.tanishtir()
print(talaba2.get_age())




















































