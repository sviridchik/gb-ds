from abc import ABC, abstractmethod


# 1
class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        s = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                s += str(self.data[i][j])
                s += " "
            s += "\n"
        return s

    def __add__(self, other):
        res = []
        for i in range(len(self.data)):
            tmp = []
            for j in range(len(self.data[0])):
                tmp.append(self.data[i][j] + other.data[i][j])
            res.append(tmp)
        return Matrix(res)


data = [
    [3, 5, 8, 3],
    [8, 3, 7, 1]
]


# m = Matrix(data)
# print(m)
# m2 = Matrix(data)
# # print(m)
# m3 = m+m2
# print(m3)

class Cloth(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def meth1(self):
        print("very import method")

    @property
    def calculate(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)


class Costume(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)


#
# coat = Coat(2, 4)
# c = Costume(1, 2)
# print(coat.calculate)
# print(c.calculate)

# 3
class Cell:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Cell(self.data + other.data)

    def __sub__(self, other):
        return Cell(int(self.data - other.data))

    def __mul__(self, other):
        return Cell(int(self.data * other.data))

    def __truediv__(self, other):
        return Cell(round(self.data // other.data))

    def make_order(self, n):
        res = ''
        for i in range(int(self.data / n)):
            res += "*" * n +'\n'
        res += "*" * (self.data % n)
        return res


cells1 = Cell(12)
cells2 = Cell(9)
print(cells1.data)
print((cells1 + cells2).data)
print((cells1 - cells2).data)
print(cells1.make_order(5))
