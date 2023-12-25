#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

lst = [2, 4, 5, 6, 7]
for i in lst:
    print('---', i)
    if i % 2 == 0:
        print(i)
        lst.remove(i)
print(lst)
