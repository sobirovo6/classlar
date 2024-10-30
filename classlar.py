class name_age:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getname(self):
        return self.__name

    def get_age(self):
        return self.__age

ism = name_age('rahmatjon', 18)
print(f"ism {ism.getname()} yosh {ism.get_age()}")

class Employee:
    def __init__(self, ism, lavozim, maosh):
        self.__ism = ism
        self.__lavozim = lavozim
        self.__maosh = maosh

    def set_salary(self, maosh1):
        if self.__lavozim == "menejer":
            self.__maosh = maosh1
            print(f"{self.__ism} uchun maosh yangilandi")
        else:
            print(f"kechirasiz faqat menejer maoshi yangilandi")

employee1 = Employee("ali", "menejer", '5000$')
employee2 = Employee("vali", "dasturchi", '3000$')

employee1.set_salary('6000$')
employee2.set_salary('5000$')


