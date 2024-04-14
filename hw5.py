def read_single_digit(num):
    if num == '0':
        return '영'
    elif num == '1':
        return '일'
    elif num == '2':
        return '이'
    elif num == '3':
        return '삼'
    elif num == '4':
        return '사'
    elif num == '5':
        return '오'
    elif num == '6':
        return '육'
    elif num == '7':
        return '칠'
    elif num == '8':
        return '팔'
    else:
        return '구'
def read_number(num):
    length = len(num)
    if length == 1:
        return read_single_digit(num)
    elif length == 2:
        return (f'{read_single_digit(num[0])} {read_single_digit(num[1])}')
    else:
        return (f'{read_single_digit(num[0])} {read_single_digit(num[1])} {read_single_digit(num[2])}')

num = input('세 자리 정수 입력:')
print(read_number(num))
