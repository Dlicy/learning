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


#鍙橀噺浣滅敤鍩�
x = 50
def func():
    global x
    print('x鐨勫師鍊�',x)
    x = 100
    print('x鐨勬敼鍙樺€�',x)

func()
print('x鐨勫€�',x)

def out_func():
    x = 5               #x涓哄閮ㄥ嚱鏁扮殑鍊�
    def inner_func():
        nonlocal x      #nonlocal鍏抽敭瀛楋紝浣垮唴閮ㄥ弬鏁板彲浠ヤ慨鏀瑰閮ㄥ弬鏁扮殑鍊�
        x = 10
    inner_func()
    print(x)
out_func()
