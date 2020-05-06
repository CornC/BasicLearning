'''
@Description: 简单的英雄和怪物战斗的小游戏
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-09 11:55:55
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-09 15:38:05
'''

from abc import ABCMeta, abstractclassmethod
from random import randint, randrange

class Role(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self.hp

    @property
    def alive(self):
        return self._hp > 0 

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >=0 else 0

    @abstractclassmethod
    def attack(self, other):
        pass

class Hero(Role):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other._hp -= randint(10, 15)

    def use_skill(self, other):

        if self._mp >= 50:
            self._mp -= 50
            damage = other._hp * 3 // 4
            damage = damage if damage >= 50 else 50
            other._hp -= damage
            return True
        else:
            self.attack(other)
            return False
    
    def use_rangeSkill(self, others):

        if self._mp >= 20:
            self._mp -= 20
            for other in others:
                if other.alive:
                    other._hp -= randint(10, 20)
            return True
        else:
            return False

    def mp_resume(self):
        self._mp += 5
        return self._mp

    def __str__(self):
        return '~~~%s~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Monster(Role):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, other):
        other._hp -= randint(7, 18)
        
    def __str__(self):
        return '~~~%s~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

def is_any_alive(monsters):

    for monster in monsters:
        if monster.alive:
            return True
    return False

def attack_target(monsters):

    monsters_len = len(monsters)

    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster

def display(hero, monsters):

    print(hero)
    for monster in monsters:
        print(monster)

def main():

    hero = Hero('Diablo', 500, 200)

    m1 = Monster('Dead_T', 400)
    m2 = Monster('Dead_DPS', 200)
    m3 = Monster('Dead_SUP', 300)

    monsters = [m1, m2, m3]

    fight_round = 1

    while hero.alive and is_any_alive(monsters):
        print('========第%02d回合========' % fight_round)
        monster = attack_target(monsters)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (hero.name, monster.name))
            hero.attack(monster)
            print('%s的魔法值恢复了%d点.' % (hero.name, hero.mp_resume()))
        elif skill <= 8:
            if hero.use_rangeSkill(monsters):
                print('%s使用了魔法攻击.' % hero.name)
            else:
                print('%s使用魔法失败.' % hero.name)
        else:
            if hero.use_skill(monster):
                print('%s使用究极必杀技虐了%s.' % (hero.name, monster.name))
            else:
                print('%s使用普通攻击打了%s.' % (hero.name, hero.name))
                print('%s的魔法值恢复了%d点.' % (hero.name, hero.mp_resume()))
        
        if monster.alive:
            print('%s使用普通攻击打了%s.' % (monster.name, hero.name))
            monster.attack(hero)
        display(hero, monsters)
        fight_round += 1
    print('\n========战斗结束!========\n')
    if hero.alive:
        print('Hero Win !')
    else:
        print('Monsters Kill You !')

if __name__ == "__main__":
    main()

