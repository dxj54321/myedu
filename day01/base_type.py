def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')
def int_test():
    aint = 5
    print(aint)
    print(type(aint))
def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))
def float_demo():
    afloat = 1.6
    print(afloat)
    print(type(afloat))
def add_demo(a,b):
    print(a+b)
def type_ZH():
    aint = 16
    print(type(aint))
    print(type (str(aint)) )
    print(type (int(aint)) )
    print(type (float(aint)) )
    print(type (int(aint)) )
def str_join():
    a = 23
    b = '小鸟'
    c = 2.5
    print('%s %s %s'%(a,b,c))
    print('a是%s b是%s c是%s'%(a,b,c))
    print(str(a)+b+str(c))
def JF_demo(a,b):
    c = a - b
    return c
if __name__ == '__main__':
    # int_test()
    # str_demo()
    float_demo()
    # add_demo(10.5,39.6)
    # add_demo('小','鸟')
    # add_demo('你好','123')
    # type_ZH()
    # str_join()
    # d = add_demo(9, 3)
    # c = JF_demo(9,3)
    # print(c)
    # print(d)
    # print(type(d))