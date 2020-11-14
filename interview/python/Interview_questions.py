#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


def print_directory_contents(path):
    """
    这个函数接收文件夹的名称作为输入参数 返回该文件夹中文件的路径 以及其包含文件夹中文件的路径
    """
    import os
    for s_child in os.listdir(path):
        s_child_path = os.path.join(path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


def day_of_year():
    """
     输入日期， 判断这一天是这一年的第几天?
    :return:
    """
    import datetime
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1-date2).days + 1


def str2dict_func1(str1):
    """
    将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
    :param str1:
    :return:
    """
    dict1 = {}
    for iterms in str1.split('|'):
        key, value = iterms.split(':')
        dict1[key] = value
    return dict1


def str2dict_func2(str1):
    """
    字典推导式
    将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
    :param str1:
    :return:
    """
    d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
    return d


def sort_by_age(list1):
    """
    请按alist中元素的age由大到小排序
    alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
    :param list1:
    :return:
    """
    return sorted(list1, key=lambda x: x['age'], reverse=True)


if __name__ == '__main__':

    print_directory_contents('/Users/hcq/code/work_recording/work')
    print(day_of_year())