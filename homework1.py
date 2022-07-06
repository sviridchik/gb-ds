# first task
def first():
    age = int(input("Enter your age  "))
    print(f" age : {age}")
    name = input("What is your name ? ")
    print(f"Hello,{name}")


# first()
# second task
def second(data_sec):
    # data_sec = int(input("Input time in seconds "))
    hour = data_sec // 3600
    minutes = data_sec // 60 % 60
    seconds = data_sec % 60
    print(f"{hour:02d}:{minutes:02d}:{seconds:02d}")
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


# data_sec = int(input("Input time in seconds "))
# second(data_sec)

def second_test():
    data_sec = 123456789
    data_sec2 = 804345
    if second(data_sec) != "34293:33:09":
        raise Exception("smth wrong")
    elif second(data_sec2) != "223:25:45":
        raise Exception("smth wrong")
    else:
        print("ok")


# second_test()
# third
# n = int(input("Enter number "))
def third(n):
    res = 0
    for i in range(3):
        elem = 0
        while i != 0:
            elem += n * 10 ** (i)
            i -= 1
        elem += n
        res += elem
    print(res)
    return res


def third_test():
    n = 3
    if third(n) != 369:
        raise Exception("error")
    else:
        print("ok")


# third_test()
# fourth task
def fourth():
    n = int(input("Enter number "))
    n_max = n % 10
    while n > 10:
        if n % 10 > n_max:
            n_max = n % 10

        n //= 10
    print(n_max)


# fourth()

def fifth():
    profit = float(input("Enter profit "))
    costs = float(input("Enter cost "))
    if profit > costs:
        print("profit is more than cost")
        profitability = (profit - costs) / profit
        people = int(input("Enter number of employees  "))
        print(f"profitability per person is {profitability / people}")
    elif profit < costs:
        print("cost is more than profit")
    else:
        print("profit and cost are equal")


# fifth()
def six(a=2, b=3):
    day = 1
    distance = a
    while distance < b:
        distance += 0.1 * a
        day += 1
    print(day)
# six()
