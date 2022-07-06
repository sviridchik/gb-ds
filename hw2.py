import re


# first task
def first():
    data = ["qwerty", 12, 12.3, [], set(), tuple(), {}, True, None, b'bla']
    for el in data:
        print(type(el))


# first()
# task2
def second():
    data = []
    raw_data = int(input("Enter values: \n"))
    # raw_data = "0 1 2 3 4 5 6"
    for el in raw_data.split():
        data.append(eval(el))
    for i in range(0, len(data) - 1, 2):
        data[i], data[i + 1] = data[i + 1], data[i]
    print(data)


# second()

# task3
def third():
    data = {"spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11], "winter": [12, 2, 3]}
    month = int(input("Enter month :\n"))
    for k, v in data.items():
        if month in v:
            print(f"this is {k}")


# third()
# task4#
def fourth():
    sentence = input()
    # sentence = "The New York Times, традиционная транскрипция «Нью-Йорк таймс» — американская ежедневная газета, издающаяся в Нью-Йорке с 18 сентября 1851 года. Третья по тиражу газета в стране после USA Today и The Wall Street Journal и 40-я в мире."
    sentence = re.sub(r'[^\w\s]', '', sentence)
    for el in sentence.split():
        # it's actually not clear for me how long is too long?
        if len(el) > 11:
            print(el[:11])
        else:
            print(el)


# fourth()
class rating(list):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def add(self, el):
        # looks like data guaranteed sorted

        if el > self.data[0]:
            self.data.insert(0, el)
        elif el <= self.data[-1]:
            self.data.append(el)
        elif el in self.data:
            self.data.insert(self.data.index(el), el)
        else:
            for i in range(len(self.data)):
                node = self.data[i]
                if el > node:
                    if i < len(self.data) - 1 and node == self.data[i + 1]:
                        continue
                    else:
                        self.data.insert(self.data.index(node), el)
                        break


# test = [7, 5, 3, 3, 2]
# l =rating(test)
# l.add(3.01)
# print(l.data)
# l.add(8)
# print(l.data)
# l.add(1)
# print(l.data)

# task6

id = 1
data = []
statistics = {"name": [], "price": [], 'amount': [], 'ed': []}
while True:
    command = input("Enter 1-if you want to add ,2-exit,3- collect statistic \n")
    if command == '1':
        node_data = {}
        node_data['name'] = input("Enter name ")
        if node_data['name'] not in statistics['name']:
            statistics['name'].append(node_data['name'])

        node_data['price'] = float(input("Enter price "))
        if node_data['price'] not in statistics['price']:
            statistics['price'].append(node_data['price'])

        node_data['amount'] = int(input("Enter amount "))
        if node_data['amount'] not in statistics['amount']:
            statistics['amount'].append(node_data['amount'])

        node_data['ed'] = input("Enter ed ")
        if node_data['ed'] not in statistics['ed']:
            statistics['ed'].append(node_data['ed'])
        data.append(tuple([id, node_data]))
        id += 1
        print(data)
        print(statistics)
    elif command == '2':
        break
    elif command == '3':
        for k, v in statistics.items():
            print(k, v)
