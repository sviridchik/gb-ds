# 1
def first():
    f = open("first",'w')
    while True:
        data = input()
        if data == '':
            break
        f.write(data+'\n')
    f.close()
# first()
# 2
def second():
    data = {"rows":0,"words":0}
    f = open("second")
    for line in f:
        data["rows"] += 1
        data["words"] += len(line.split())

    print(data)
# second()
# 3
def third():
    data_output = []
    data_profit = []
    with open("third", "r") as f:
        for line in f.readlines():
            if eval(line.split()[-1]) < 20000:
                data_output.append(line.split()[0])
            data_profit.append(eval(line.split()[-1]))
    print(data_output)
    print(sum(data_profit)/len(data_profit))
# third()
# 4
def fourth():
    data = {'One':'один','Two':'два','Three':'три','Four':'четыре'}
    f_output = open('fourth_output','w')
    with open("fourth", "r") as f:
        for line in f.readlines():
            s=""
            s=s+data[line.split('—')[0]]+'—'+line.split('—')[-1]
            f_output.write(s)

# fourth()
def fifth():
    data = '1 2 3 4 5 6 7'
    with open("fifth", "w") as f:
        f.write(data)
    with open("fifth", "r") as f:
        data = f.read()
        print(data)
        print(sum([eval(el) for el in data.split()]))
# fifth()


def six():
    data = {}
    with open("six", "r") as f:
        for line in f.readlines():
            node = line.split()
            data[node[0]] = 0
            res = 0

            for i in range(1, len(node)):
                el = node[i].split("(")[0]
                if el != '—':
                    res+= eval(node[i].split("(")[0])
            data[node[0]] = res
        print(data)

# six()
def seventh():
    data_profit = {}
    not_profit ={}
    profit_list = []
    with open("seventh", "r") as f:
        for line in f.readlines():
            node = line.split()
            print(node)
            profit = eval(node[2]) - eval(node[3])
            if profit<0:
                not_profit[node[0]]=abs(profit)
            else:
                data_profit[node[0]]  = profit
                profit_list.append(profit)
        data_profit["average_profit"] = sum(profit_list)/len(profit_list)
        print("profit", data_profit)
        print("no profit", not_profit)
seventh()
