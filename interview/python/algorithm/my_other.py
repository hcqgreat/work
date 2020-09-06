#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class MyAlgorithm:

    def multiplication_table_one(self):
        """
            第一种方法实现9*9乘法表
        :return:
        """
        return print(
            '\n'.join(['\t'.join(['{}*{}={}'.format(x, y, x * y) for x in range(1, y + 1)]) for y in range(1, 10)]))

    def multiplication_table_two(self):
        """
            第二种方法实现9*9乘法表
        :return:
        """
        for i in range(1, 10):
            for j in range(1, i + 1):
                print('%s*%s=%s' % (i, j, i * j), end='\t')
            else:
                print()


al = MyAlgorithm()
al.multiplication_table_two()
al.multiplication_table_one()
