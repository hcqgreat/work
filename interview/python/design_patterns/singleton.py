#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class MySingletonOneClass:
    """
        单例设计模式  ----> 第一种
        单例模式(Singleton Pattern)的核心作用是确保一个类只有一个实例，并且提供一 个访问该实例的全局访问点
    """

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingletonOneClass.__init_flag:
            print("init")
            self.name = name
            MySingletonOneClass.__init_flag = False


class MySingletonTwoClass:
    """
        单例设计模式 ----> 第二种
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(MySingletonTwoClass, cls)
            cls._instance = org.__new__(cls)

        return cls._instance


singleton_one = MySingletonOneClass('test')
