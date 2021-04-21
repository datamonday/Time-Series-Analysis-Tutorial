a = 10
b = 2
d = []

def fn():
    print('Hello fn')
    fn2()

def fn2():
    print('Hello fn2')
    fn3()

def fn3():
    print('Hello fn3')
    5/0

fn()    