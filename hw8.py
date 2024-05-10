def buy(shopping_bag):
    name = input('[구입]\n상품명?')
    if name == '':
        return False
    else:
        n = int(input('수량은?'))
        shopping_bag[name] = n
        print(f'장바구니에 {name} {n}개가 담겼습니다.\n')

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기:{shopping_bag}\n')
        
def find(shopping_bag):
    name = input('[검색]\n장바구니에서 확인하고자 하는 상품은?')
    if name in shopping_bag:
        print(f'{name}은(는) {shopping_bag[name]}개 담겨있습니다.')
    else:
        print(f'장바구니에 {name}은(는) 없습니다.')
        
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
        
