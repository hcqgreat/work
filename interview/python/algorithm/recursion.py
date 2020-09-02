#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

class Recursion():
    '''
        递归算法----->自己调用自己
        递归结构包括两个部分:
         定义递归头。解答:什么时候不调用自身方法。如果没有头，将陷入死循环，也就是递归的结束条件。
         递归体。解答:什么时候需要调用自身方法。
    '''

    def factorial(self, n):
        '''
        利用递归算法，计算n的阶乘
        :param n:
        :return: n!
        '''
        if n == 1 :
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci_sequence(self, n):
        '''
        斐波那契数列
        :return: 数列
        '''

        list = []
        a, b = 0, 1
        while a < n:
            list.append(a)
            a, b = b, a +b
        return list


    def getAllFiles(self, path, level):
        '''
        利用递归，展示目录树
        :param path:
        :return: 目录树
        '''
        import os
        childFiles = os.listdir(path)
        allFiles = []
        for file in childFiles:
            filepath = os.path.join(path,file)
            if os.path.isdir(filepath):
                self.getAllFiles(filepath,level + 1)
            allFiles.append("\t" * level + filepath)

        for f in reversed(allFiles):
            print(f)


if __name__ == '__main__':
    recursion = Recursion()
    #test = recursion.factorial(5)
    #print(test)

    # recursion.getAllFiles("/Users/work/code/python/Pythonbase/",0)

    list = recursion.fibonacci_sequence(100)
    print(list)