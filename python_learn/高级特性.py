#from collections.abc import Iterable
#print(isinstance('abc', Iterable))


#python鍐呯疆浜唀numerate鍑芥暟
#for i,value in enumerate (['a','s','d']):
#    print(i,value)


#print([list(range(1,11))])      #鍒涘缓0-10鐨勫垪琛�
#print([x * x for x in range(1,11)])
#print([x * x for x in range(1,11) if x % 2 == 0])
#print([m + n for m in 'ABC' for n in 'ZXC'])

#print([x if x % 2 ==0 else -x for x in range(1,11)])

#g = (x*x for x in range (1,11))
#for n in g:
#    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
#print(next(o))
#print(next(o))
print(next(odd()))
print(next(odd()))
#odd()浼氬垱寤轰竴涓柊鐨刧enerator瀵硅薄锛屼笂杩颁唬鐮佸疄闄呬笂鍒涘缓浜�2涓畬鍏ㄧ嫭绔嬬殑generator
#瀵�2涓猤enerator鍒嗗埆璋冪敤next()褰撶劧姣忎釜閮戒細杩斿洖绗竴涓€�

#print(isinstance((x for x in range(10)), Iterator))
#print(isinstance([], Iterator))
#print(isinstance(iter([]), Iterator)) #浣跨敤iter()鍑芥暟灏嗗彲杩唬瀵硅薄鍙樻垚杩唬鍣ㄥ璞�
