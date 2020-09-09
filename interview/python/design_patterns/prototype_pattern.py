#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang


from copy import copy, deepcopy


class Prototype:
    """
        原型抽象类
    """
    def clone(slef):
        pass

    def deep_clone(self):
        pass


class WorkExperience:
    """
        work experience类
    """
    def __init__(self):
        self.time_area = ''
        self.company = ''

    def set_work_experience(self, time_area, company):
        self.time_area = time_area
        self.company = company


# Resume类
class Resume(Prototype):
    def __init__(self, name):
        self.name = name
        self.work_experience = WorkExperience()

    def set_person_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, time_area, company):
        self.work_experience.set_work_experience(time_area, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('work experience', self.work_experience.time_area, self.work_experience.company)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    obj1 = Resume('uu')
    obj2 = obj1.clone()
    obj3 = obj1.deep_clone()

    obj1.set_person_info('male', 28)
    obj1.set_work_experience('2001-2003', 'developing')
    obj2.set_person_info('male', 26)
    obj2.set_work_experience('2004-2006', 'BA')
    obj3.set_person_info('male', 26)
    obj3.set_work_experience('2011-2012', 'testing')

    obj1.display()
    obj2.display()
    obj3.display()
