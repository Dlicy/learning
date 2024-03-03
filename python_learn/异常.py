#捕获异常
#提前假设某处会出现异常，并提前准备
#捕获异常的作用，可以防止程序因为一个小bug而无法运行

#语法：
#try:
    #可能出现问题的代码
#except:
    #如果出现异常，执行的代码

#捕获指定的异常

try:
    #print(name)
#except NameError as e:
    print('')

#捕获多个异常
#将要捕获的异常类型的名字，以元组的形式放在except后
#except ('NameError'，'ZeroDivisionError') as e:

#捕获全部的异常
except Exception as e :

#Exception为顶级的异常，是所有异常的父类

#异常else
#try:

#except:

#else:
    #没有异常时执行的代码

#异常finally
#try:

#except:

#else:

#finally:
    #无论是否异常，都会执行的代码


#异常的传递
#当有异常的函数被调用，异常就会按照运行顺序一直传递下去