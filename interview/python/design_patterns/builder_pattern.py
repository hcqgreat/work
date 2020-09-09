#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class Burger:
    """
    主食类，价格名字
    """
    name = ""
    price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class CheeseBurger(Burger):
    """
    奶酪汉堡
    """

    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    """
    香辣鸡汉堡
    """

    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack:
    """
    小食类，价格以及名字
    """
    name = ""
    price = 0.0
    type = "SNACK"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Chips(Snack):
    """
    炸薯条
    """

    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class ChickenWings(Snack):
    """
    鸡翅
    """

    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage:
    """
    饮料
    """
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    """
    可乐
    """

    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    """
    牛奶
    """

    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class Order:
    """
    订单对象，一个订单中包含一份主食，一份小食，一份饮料
    """
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Burger:%s" % self.burger.get_name())
        print("Snack:%s" % self.snack.get_name())
        print("Beverage:%s" % self.beverage.get_name())


# 建造者
class OrderBuilder:
    """
    orderBuilder就是建造者模式中所谓的“建造者”，
    将订单的建造与表示相分离，以达到解耦的目的。
    在上面订单的构建过程中，如果将order直接通过参数定义好（其构建与表示没有分离），
    同时在多处进行订单生成，此时需要修改订单内容，
    则需要一处处去修改，业务风险也就提高了不少。
    """
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def add_burger(self, xBurger):
        self.bBurger = xBurger

    def add_snack(self, xSnack):
        self.bSnack = xSnack

    def add_beverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return Order(self)


# Director类
class OrderDirector:
    """
    在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。
    对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。
    """
    order_builder = ""

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def create_order(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


# 场景实现
if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.add_burger(SpicyChickenBurger())
    order_builder.add_snack(Chips())
    order_builder.add_beverage(Milk())
    order_1 = order_builder.build()
    order_1.show()
