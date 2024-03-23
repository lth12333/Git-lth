def get_integer(prompt):
    cost = int(input(prompt))
    return cost

def exchange(cost):
    n500 = cost // 500
    cost %= 500
    n100 = cost // 100
    cost %= 100
    n50 = cost // 50
    cost %= 50
    n10 = cost // 10
    print('500원 동전의 갯수 :', n500, '\n100원 동전의 갯수 :', n100, '\n50원 동전의 갯수 :', n50, '\n10원 동전의 갯수 :', n10)

cost = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(cost)
