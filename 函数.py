def cal(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    #print(sum)
    return sum

nums = [1,2,3]

cal(*nums)


def person(name,age,**kw):
    print('name:',name,'age:','other:',kw)

person('bob',34,city='beijing')


#变量作用域
x = 50
def func():
    global x
    print('x的原值',x)
    x = 100
    print('x的改变值',x)

func()
print('x的值',x)

def out_func():
    x = 5               #x为外部函数的值
    def inner_func():
        nonlocal x      #nonlocal关键字，使内部参数可以修改外部参数的值
        x = 10
    inner_func()
    print(x)
out_func()
