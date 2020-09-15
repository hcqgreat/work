#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class MySort:
    """
        五种排序方法
        １、冒泡排序
        ２、选择排序
        ３、插入排序
        ４、快速排序
        ５、希尔排序
    """

    def bubble_sort(self, lst):
        """
            冒泡排序
        :param lst: 
        :return: 
        """
        n = len(lst)
        for k in range(n - 1):
            count = 0
            for i in range(n - 1 - k):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    count += 1
            if count == 0:
                break
                
    def select_sort(self, lst):
        """
            选择排序
        :param lst:
        :return:
        """
        n = len(lst)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n - 1):
                if lst[min_index] > lst[j]:
                    min_index = j
            if min_index != i:
                lst[i], lst[min_index] = lst[min_index], lst[i]
            
    def insert_sort(self, lst):
        """
            插入排序
        :param lst: 
        :return: 
        """
        for i in range(1, len(lst)):
            while i > 0:
                if lst[i] < lst[i - 1]:
                    lst[i], lst[i - 1] = lst[i - 1], lst[i]
                else:
                    break
                i -= 1
                
    def quick_sort(self, lst):
        """
            快速排序
        :param lst: 
        :return: 
        """
        if len(lst) >= 2:  # 递归入口及出口        
            mid = lst[len(lst) // 2]  # 选取基准值，也可以选取第一个或最后一个元素        
            left, right = [], []  # 定义基准值左右两侧的列表        
            lst.remove(mid)  # 从原始数组中移除基准值        
            for num in lst:
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            return quick_sort(left) + [mid] + quick_sort(right)
        else:
            return lst
        
    def shell_sort(self, lst):
        """
            希尔排序
        :param lst:
        :return:
        """
        n = len(lst)
        step = n // 2
        while step > 0:
            for cur in range(step, n):
                i = cur
                while i >= step and lst[i-step] > lst[i]:
                    lst[i - step], lst[i] = lst[i], lst[i-step]
                    i -= step
            step = step // 2