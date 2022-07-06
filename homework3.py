# first task
def first(a, b):
    if b == 0:
        raise Exception("Division by zerro")
    else:
        return a / b


def test_first():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(first(a, b))


# test_first()

def second(name, fam_name, year, city, email, phone):
    print(f"name :{name} fam_name :{fam_name} year :{year} city :{city} email :{email} phone :{phone} ")


second(name="vikusha", fam_name="fam name", year=2000, city="minsk", email="test@gmai.com", phone=12323)


def third(a, b, c):
    sum_data = []
    data = [a, b, c]
    sum_data.append(max(data))
    data.remove(sum_data[0])
    sum_data.append(max(data))
    return sum(sum_data)


# print(third(-9,5,-3))
def fourth(x, y):
    print(x ** y)
    res = 1
    for i in range(abs(y)):
        res *= (1 / x)
    print(res)


# fourth(2,-2)
def fifth():
    data = []
    while True:
        a = list(input('Введите числа: ').split())
        try:
            a = [eval(el) for el in a]
            data = data + a
            print(sum(data))
        except Exception:
            break


# fifth()

def six(args):
    # for el in args:
    #     el.title()
    res = [el.title() for el in args]
    # print(res)
    return res


args = ["hi", "name", "bla"]


# six(args)


# not clear when to stop
def seventh():
    data = []
    while True:
        a = list(input('Введите слова: ').split())
        try:
            a = six(a)
            data = data + a
            # print(sum(data))
            res = " ".join(data)
            print(res)
        except Exception:
            break


seventh()
