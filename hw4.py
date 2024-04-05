name = input('input his/her name :')

def rep_char(shape, num):
    print(shape * int(num))

def draw_line_string(msg):
    msg1 = 'hello {}'.format(msg)
    msg2 = 'welcome to seoul'
    if len(msg1) >= len(msg2) :
        length = len(msg1) + 2
    else :
        length = len(msg2) + 2
    rep_char('-',length)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-',length)

draw_line_string(name)
