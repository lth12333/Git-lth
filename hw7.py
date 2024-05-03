shopping_bag = {}
while True:
    item = input('상품명?')
    if item == '':
        break
    else:
        item_n = (input('수량은?'))
        shopping_bag[item] = int(item_n)
        print(f'장바구니에 {item} {item_n}개가 담겼습니다.')
print(f'>>> 장바구니 보기:{shopping_bag}')
print('\n[검색]')
item = input('장바구니에서 확인하고자 하는 상품은?')
print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')

