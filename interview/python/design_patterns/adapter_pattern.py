#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

# target, 需要安卓的充电线


class Android:
    def __init__(self):
        pass

    def connect_mobile(self, mobile):
        print('我是安卓手机，需要安卓手机充电线')
        mobile.connectAn()


# adapter
class Adapter:
    def __init__(self):
        self._connectApple = Apple()

    def connectAn(self):
        print('适配器来了，是个转换接口，苹果充电线接上适配器就能给安卓手机充电了')
        self._connectApple.connectAp()


# adaptee , 这是个苹果手机的充电线
class Apple:
    def __init__(self):
        pass

    def connectAp(self):
        print('有苹果手机充电线')


if __name__ == '__main__':
    androidM = Android()
    adapter = Adapter()
    androidM.connect_mobile(adapter)