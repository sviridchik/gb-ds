from time import sleep


# 1
class TrafficLight:

    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for el in self.__color:
            print(f"color : {el}")
            if el == 'Красный':
                sleep(7)
            elif el == 'Желтый':
                sleep(2)
            else:
                sleep(9)


# t = TrafficLight()
# print(t)
# t.running()

# 2
class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def count_mass(self, weight, thickness=1):
        print(
            f"weight {self._width * self._length * weight * thickness} kg {(self._width * self._length * weight * thickness) / 1000} t")
        self.weight = self._width * self._length * weight


#
# r = Road(20,5000)
# r.count_mass(25,5)

# 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


p = Position('Name', 'Surname', 'CoolJob', 520, 250)


# print(p.get_full_name())
# print(p.position)
# print(p.get_total_income())
# 3#

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is started')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} is turned {direction}')

    def show_speed(self):
        print( f'Current speed : {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Too much! : {self.speed}')
        else:
            print(f'Current speed : {self.speed}')

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Too much! : {self.speed}')
        else:
            print(f'Current speed : {self.speed}')

# car1 = WorkCar(100, 'Red', 'Bla', False)
# car1.show_speed()
# car2 = TownCar(100, 'Red', 'Bla', False)
# car2.show_speed()
# car3 = TownCar(40, 'Red', 'Bla', False)
# car3.show_speed()
# 5#
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print( f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print( f'Запуск отрисовки via pen {self.title}')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print( f'Запуск отрисовки via Pencil {self.title}')

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print( f'Запуск отрисовки via Handle {self.title}')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()
