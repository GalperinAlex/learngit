

def all_actions():
    try:
        actions_A()
        actions_B()
    except ZeroDivisionError:
        print('Somewhere divide by zero')

def actions_A():
    try:
        actionA1(0)
        actionA2(19)
    except ValueError:
        print('A function got num > 10')


def actions_B():
    actionB1(8)
    actionB2(0)



def actionA1(num):
    if num>10:
        raise ValueError
    x = 10/num
    print('actionA1')

def actionA2(num):
    if num>10:
        raise ValueError
    x = 10/num
    print('actionA2')

def actionB1(num):
    x = 10/num
    print('actionB1')

def actionB2(num):
    x = 10/num
    print('actionB2')

all_actions()
