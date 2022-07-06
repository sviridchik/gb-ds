import sys
from functools import reduce
from itertools import count, cycle


def first():
    if len(sys.argv)!=4:
        raise Exception("wrong number of parameters")
    for el in  sys.argv[1:]:
        if isinstance(eval(el),float) or isinstance(eval(el),float):
            raise Exception("wrong type")
    print((eval(sys.argv[1])*eval(sys.argv[2])) + eval(sys.argv[3]))

# first()
data2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def second(data2):
    print([data2[i]  for i in range(1,len(data2)) if data2[i] > data2[i-1]])
# second(data2)

def third():
    print([el for el in range(20,240,1) if (el%20 == 0 or el%21 == 0)])
# third()

data4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def fourth(data4):
    print([el for el in data4 if data4.count(el) == 1 ])
# fourth(data4)
def my_func(prev_el, el):
    el = prev_el * el
    return el
def fifth():
    data = [el for el in range(100,1001,1) if el%2==0]
    # print(data)
    print(reduce(my_func, data))
# fifth()

def six(start=3, stop=10,data5=["QWERTY","hi",2,3]):
    for el in count(start):
        if el > 10:
            break
        else:
            print(el)

    c = 0
    for el in cycle(data5):
        if c > stop:
            break
        print(el)
        c += 1
# six()
def seventh(x):
        res = 1
        for i in range(1, x + 1):
            res *= i
            yield res

# print(next(seventh(3)))
amount = 6
res = [el for el in seventh(amount)]
# print(res)
