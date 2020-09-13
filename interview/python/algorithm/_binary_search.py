#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

def binary_search(arr, target):
    '''
    二分查找
    :param arr:
    :param target:
    :return:
    '''
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            print(f"index：{mid},value：{arr[mid]}")
            return True
    return False

if __name__ == '__main__':
    l = [1, 3, 4, 5, 6, 7, 8]
    binary_search(l, 8)