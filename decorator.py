#coding:utf-8
#decorator���þ����ڵ��ú���ʱ���Ե��ý��С��ض��򡱣�
#����funcʱ��ͬʱ�������funcʱ���Ĳ����������ڡ�func����
#���Խ��е���ǰ�Ķ��⴦�����ز������ĺ�����
#Ҳ���ԡ��ض��򡱵�����������
#decorator�ķ���ֵ�����Ǻ���
#�ɶ��Ƕ��
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

#@���Ż������Ӧdecoratorһ�Σ���ʹ��δ����func1����
#Ϊ�˽��������⣬��decorator��ֻ���岻ִ������inner decorator
#���£��������inner decorator���൱����д��func2
#����decorator2��ʵ������Ԥ����,��func��װ
#def decorator2(func):
#    print("pre-pocessing")
#    def decorator(x):
#        print("real decorator")
#        return func(x) #func���ص��Ǻ������������ص��Ǻ�������Ҫִ��func��func(x)
#    return decorator  #func2ָ���µķ��غ���decorator,����func2���ǵ���decorator
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


#���decorator������Ҫ����������Ҫ�ٶ�һ���װ
#�����շ��ز�����ԭfunc�ĺ���wrapper,����һ�㺯���Ĳ���ֻ����func
#Ҳ����˵��ԭ����func5��Ϊ����������һ��û��ָ��������װ�κ���
#���������logʱָ����text����func5����decorator��func,���func5Ϊdecorator�ķ��غ���������˭����˭�ķ���)
def log(text): 
    def decorator(func):
        #@functools.wrap(func) #�޸����շ��غ���wrapper�����ƺ�ԭ������ͬ
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
