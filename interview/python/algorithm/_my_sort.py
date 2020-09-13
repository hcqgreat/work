#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


class MySort:
    """
        排序方法
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
        mid = lst[0]
        low = 0
        high = len(lst) - 1

        while lst[high] > mid and low < high:
            high -= 1
        lst[low] = lst[high]