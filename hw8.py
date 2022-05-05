import math


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        answ =[int(el) for el in day_month_year.split(":")]
        return answ

    @staticmethod
    def valid(data):
        day, month, year = data
        data = ['day','month', 'year']
        etalon = [1 <= day <= 31 ,  1 <= month <= 12 , year>=0]
        if 1 <= day <= 31 and  1 <= month <= 12 and year>=0:
            print("cool")
        else:
            for i in range(3):
                if not etalon[i]:
                    print(f"problems with {data[i]}")

    def __str__(self):
        return f'{Data.extract(self.day_month_year)}'

#
# d = Data('01:05:2022')
# print(d)
# Data.valid(Data.extract('05:05:2022'))
# Data.valid(Data.extract('05:05:-2022'))
# Data.valid(Data.extract('95:05:-2022'))


class MyException:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def check(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Exception!! Division by zero")


# e = MyException(900, 100)
# print(MyException.check(10, 0))
# print(e.check(100, 0))



class Error:
    def __init__(self, *args):
        self.data = []

    def __str__(self):
        return f"{self.data}"

    def task(self):

        while True:
            n = input('Enter number ')
            if isinstance(eval(n), int) or isinstance(eval(n),  float):
                self.data.append(eval(n))
                print(self.data)
            elif n == "exit":
                return
            else:
                print(f"invali type {type(n)}")


# try_except = Error()
# print(try_except.task())

class OrgTechik:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = []


    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Unit ')
            price = input(f'Price ')
            amount = int(input(f'amount '))
            data = {"unit":unit,'price':price,'amount':amount}
            self.stock.append(data)
        except:
            return f'INVALID INPUT'

    def get_stock(self):
        return self.stock



class Printer(OrgTechik):

    def __init__(self, name, price,capacity):
        super().__init__(name, price)
        self.capacity = capacity

    @staticmethod
    def to_print():
        return 'printing'


class Scanner(OrgTechik):
    def __init__(self, name, price,model):
        super().__init__(name, price)
        self.model = model

    @staticmethod
    def to_scan():
        return 'scanning'


class Copier(OrgTechik):

    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    @staticmethod
    def to_copier():
        return 'copying'

# o =OrgTechik("bla", 12)
# unit_1 = Printer('hp', 1000, 7)
# unit_2 = Scanner('Canon', 120,"cool")
# unit_3 = Copier('Xerox', 1900, 23)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())
#


class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a,self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return  Complex(self.a * other.a - (self.b * other.b),self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b} * i'


z_1 = Complex(1, -2)
z_2 = Complex(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
