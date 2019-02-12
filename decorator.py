#coding:utf-8
#decorator作用就是在调用函数时，对调用进行“重定向”，
#传入func时，同时传入调用func时给的参数，都含在“func”中
#可以进行调用前的额外处理（返回参数给的函数）
#也可以“重定向”调用其他函数
#decorator的返回值必须是函数
#可多层嵌套
#def decorator(func):
#    print("in decorator") 
#    def func2():
#        print("func2")
#    return func
#
#@decorator
#def func1(x):
#    print("func1")
#    print(x)
#func1(2)

#@符号会调用相应decorator一次，即使还未调用func1本身
#为了解决这个问题，在decorator内只定义不执行语句的inner decorator
#如下，返回这个inner decorator，相当于重写了func2
#定义decorator2其实就是作预处理,将func包装
#def decorator2(func):
#    print("pre-pocessing")
#    def decorator(x):
#        print("real decorator")
#        return func(x) #func返回的是函数名，即返回的是函数；若要执行func，func(x)
#    return decorator  #func2指向新的返回函数decorator,调用func2就是调用decorator
#
#@decorator2
#def func2(x):
#    print(x)
#    print("in func2")
#
#func2(2)
#
#def mutiDecorator(text):
#    def hidecorator(func):
#        print(text)
#        print("in mutiDecorator")
#        return func
#    return hidecorator 
#
#@mutiDecorator('hello')
#def func4():
#    print("func3")

#func3()


#如果decorator本身需要带参数，则要再多一层包装
#即最终返回并覆盖原func的函数wrapper,其上一层函数的参数只能是func
#也就是说，原函数func5作为参数传给第一个没有指定参数的装饰函数
#在这里，调用log时指定了text，则func5传给decorator的func,最后func5为decorator的返回函数（传给谁接收谁的返回)
def log(text): 
    def decorator(func):
        #@functools.wrap(func) #修改最终返回函数wrapper的名称和原函数相同
        def wrapper(*args, **kws):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kws)
        return wrapper
    return decorator

@log(' ')
def func5():
    print("in func5")

print(func5.__name__)
func5()


def metric(fn):
    def wrapper(*args,**kws):
        print()
