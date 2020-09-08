#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class Benz:
    print("创建奔驰")


class BMW:
    print("创建宝马")


class BYD:
    print("创建比亚迪")


class CarFactory(object):
    """
        工厂模式
    """

    def car_factory(self, brand):
        """
        工厂方法
        :param brand:
        :return:
        """
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"
