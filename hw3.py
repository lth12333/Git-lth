def get_fixed_price(per, p_price):
    return p_price * 100 / (100 - per)
per = int(input('할인율은?'))
A = int(input('A상품의 할인된 가격은?'))
B = int(input('B상품의 할인된 가격은?'))
print('A상품의 정가는', int(get_fixed_price(per, A)), '원')
print('B상품의 정가는', int(get_fixed_price(per, B)), '원')
