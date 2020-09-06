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

    def compression_str(self, s: str):
        """
            把a='aaabbcccdddde'这种形式的字符串，压缩成a3b2c3d4e1这种形式
        :return:
        """
        a = s
        aa = ''
        for i in sorted(list(set(a)), key=a.index):
            aa = aa + i + str(a.count(i))
        print(aa)

    def finish_count(self, num):
        """
            一个数如果恰好等于它的因子之和，这个数就称为‘完数’，比如6=1+2+3，编程找出1000以内的所有的完数。
        :return:
        """
        wanshu = list()
        for i in range(1, num):
            s = 0
            for j in range(1, i//2+1):
                if i % j == 0:
                    s += j
            if i == s:
                wanshu.append(i)
        print(wanshu)


al = MyAlgorithm()
al.multiplication_table_two()
al.multiplication_table_one()
al.finish_count(1000)
