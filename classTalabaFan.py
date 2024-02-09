class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

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

    def get_age(self, yil):
        """Talabaning yoshini qaytaruvchi funksiya"""
        return yil - self.tyil


class Fan:
    """ Talana nomli class yaratamiz"""
    def __init__(self,nomi):
         """Talabaninfg xususiyatlari"""
         self.nomi = nomi
         self.talaba_soni = 0
         self.talabalar = []

    def add_student(self,talaba):
        """Fanga talaba qo'shish"""
        self.talabalar.append(talaba)
        self.talaba_soni += 1
    def get_talabaler(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def get_name(self):
        """Fan nomi"""
        return self.nomi
    def get_talabalar_soni(self):
        """Talabalr sonini qaytaruvchi metod"""
        return self.talaba_soni




matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
print(matematika.talaba_soni)
mat_talabalat = matematika.get_talabaler()
print(mat_talabalat)

def see_metods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_metods(Talaba))

print(talaba1.__dict__.keys())












































