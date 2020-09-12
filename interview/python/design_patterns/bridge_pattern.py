#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

class people:
    def set_skill(self, skill):
        self.skill = skill

    def perform_skill(self):
        pass


# 具体抽象类:花匠
class hua_j(people):
    def perform_skill(self):
        print('我是花匠')
        self.skill.perform_skill()


# 具体抽象类:木匠
class mu_j(people):
    def perform_skill(self):
        print('我是木匠')
        self.skill.perform_skill()


# 具体抽象类:铁匠
class tie_j(people):
    def perform_skill(self):
        print('我是铁匠')
        self.skill.perform_skill()


# 功能类，也是实现类
class skill:
    def perform_skill(self):
        pass


# 具体功能类，也是具体实现类 种花
class skill_hua(skill):
    def perform_skill(self):
        print('我会种花')


# 具体功能类，也是具体实现类 做木桌子
class skill_mu:
    def perform_skill(self):
        print('我会做木桌子')


# 具体功能类，也是具体实现类 做铁桌子
class skill_tie:
    def perform_skill(self):
        print('我会做铁桌子')


# 具体功能类，也是具体实现类 做老师
class skill_teacher:
    def perform_skill(self):
        print('我会做老师，可以教学生')


# 具体功能类，也是具体实现类 做家具
class skill_jj:
    def perform_skill(self):
        print('我会做家具')


def main():
    h = hua_j()  # 花匠
    m = mu_j()  # 木匠
    t = tie_j()  # 铁匠

    sh = skill_hua()  # 本事:会种花
    sm = skill_mu()  # 本事:会做木头桌子
    st = skill_tie()  # 本事:会做铁桌子
    s_t = skill_teacher()  # 本事:会教学生
    s_jj = skill_jj()  # 本事:会做家具

    h.set_skill(sh)  # 给花匠set种花的本事
    h.perform_skill()  # 花匠 种花
    h.set_skill(s_t)  # 给花匠set做老师的本事
    h.perform_skill()  # 花匠教学生

    print('=============')
    m.set_skill(sm)  # 给木匠set 做木桌子的本事
    m.perform_skill()  # 木匠 做木桌子
    m.set_skill(s_t)  # 给木匠set做老师的本事
    m.perform_skill()  # 木匠教学生
    m.set_skill(s_jj)  # 给木匠set做家具的本事
    m.perform_skill()  # 木匠做家具

    print('=============')
    t.set_skill(st)  # 给木匠set 做木桌子的本事
    t.perform_skill()  # 木匠 做木桌子
    t.set_skill(s_t)  # 给木匠set做老师的本事
    t.perform_skill()  # 木匠教学生
    t.set_skill(s_jj)  # 给木匠set做家具的本事
    t.perform_skill()  # 木匠做家具


if __name__ == '__main__':
    main()