#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class RecursionClass:
    """
        递归算法----->自己调用自己
        递归结构包括两个部分:
         定义递归头。解答:什么时候不调用自身方法。如果没有头，将陷入死循环，也就是递归的结束条件。
         递归体。解答:什么时候需要调用自身方法。
    """

    def factorial(self, n):
        """
            利用递归算法，计算n的阶乘
            :param n:
            :return:
        """

        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci_sequences(self, n):
        """
            斐波那契数列
            :param n:
            :return: 数列
        """
        lst = []
        a, b = 0, 1
        while a < n:
            lst.append(a)
            a, b = b, a + b
        return lst

    def get_all_files(self, path, level):
        """
            利用递归，展示目录树
            :param path:
            :param level:
            :return: 目录树
        """
        import os
        child_files = os.listdir(path)
        all_files = []
        for file in child_files:
            filepath = os.path.join(path,file)
            if os.path.isdir(filepath):
                self.get_all_files(filepath,level + 1)
            all_files.append("\t" * level + filepath)

        for f in reversed(all_files):
            print(f)


if __name__ == '__main__':
    recursion = RecursionClass()
    # test = recursion.factorial(5)
    # print(test)

    # recursion.getAllFiles("/Users/work/code/python/Pythonbase/",0)

    lst = recursion.fibonacci_sequences(100)
    print(lst)
