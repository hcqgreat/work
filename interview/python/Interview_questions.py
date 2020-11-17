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


def reverse(x):
    """
    反转一个整数，如123 -> 321
    :param x:
    :return:
    """
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[1:][::-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


def get_missing_letter(a):
    """
    全字母短句 PANGRAM 是包含所有英文字母的句子，比如:A QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
    定义并实现一个方法 get_missing_letter, 传入一个字符串采纳数，返回参数字符串变成一 个 PANGRAM 中所缺失的字符。
    应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字 母顺序排序(请忽略所有非 ACSII 字符)
    :param a:
    :return:
    """
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set(a.lower())
    ret = "".join(sorted(s1-s2))
    return ret

    # other ways to generate letters # range("a", "z")
    # 方法一:
    # import string
    # letters = string.ascii_lowercase
    # 方法二:
    # letters = "".join(map(chr, range(ord('a'), ord('z') + 1)))


def atoi1(s):
    """
    字符串 转换成 ，不使用内置api，例如int(); 方法一:
    :param s:
    :return:
    """
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j
    return num


def atoi2(s):
    """
    字符串 转换成 ，不使用内置api，例如int(); 方法二:
    :param s:
    :return:
    """
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord('0')
    return num


def atoi3(s):
    """
    字符串 转换成 ，不使用内置api，例如int(); 方法三:
    :param s:
    :return:
    """

    num = 0
    for v in s:
        t = "%s * 1" % v
        n = eval(t)
        num = num * 10 + n
    return num


def atoi4(s):
    """
    字符串 转换成 ，不使用内置api，例如int(); 方法四:
    :param s:
    :return:
    """

    from functools import reduce
    return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s, 0)


def two_sum(nums, target):
    """
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
    你可以假设每个输入只对应一种答 案，且同样的元素不能被重复利用。
    示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    size = 0
    while size < len(nums):
        if target - nums[size] in d:
            if d[target - nums[size]] < size:
                return [d[target - nums[size]], size]
            else:
                d[nums[size]] = size
            size = size + 1


def two_sum2(nums, target):
    """
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
    你可以假设每个输入只对应一种答 案，且同样的元素不能被重复利用。
    示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        num = target - nums[i]
        if num in nums[i + 1:]:
            return [i, nums.index(num, i + 1)]


def count_words1(filepath):
    """
    统计一个文本中单词频次最高的10个单词
    :param filepath:
    :return:
    """
    import re
    distone = {}
    with open(filepath) as f:
        for line in f:
            line = re.sub("\W+", " ", line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1
    num_ten = sorted(distone.items(), key=lambda x:x[1], reverse=True)[:10]
    num_ten = [x[0] for x in num_ten]
    return num_ten


def count_words2(filepath):
    """
    统计一个文本中单词频次最高的10个单词
    :param filepath:
    :return:
    """
    import re
    from collections import Counter
    with open(filepath) as f:
        return list(map(lambda c: c[0],
                        Counter(re.sub("\W+",
                                       " ",
                                       f.read()).split()).most_common(10)))


def num_list(num):
    """
    该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件:
     1、该元素是偶数
     2、该元素在原list中是在偶数的位置(index是偶数)
    :param num:
    :return:
    """
    return [i for i in num if i % 2 == 0 and num.index(i) % 2 == 0]


def loop_merge_sort(l1, l2):
    """
    两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
    :param l1:
    :param l2:
    :return:
    """
    tmp = []
    while len(l1)>0 and len(l2)>0:
        if l1[0] <l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    while len(l1) > 0:
        tmp.append(l1[0])
        del l1[0]
    while len(l2) > 0:
        tmp.append(l2[0])
        del l2[0]
    return tmp


def func1(l):
    """
    给定一个任意长度数组，实现一个函数
    让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'
    :param l:
    :return:
    """
    if isinstance(l, str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print(''.join(str(e) for e in l))

    # def func2(l):
    #     print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))))


if __name__ == '__main__':

    print_directory_contents('/Users/hcq/code/work_recording/work')
    print(day_of_year())
    print(get_missing_letter("python"))