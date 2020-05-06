'''
@Description: Craps赌博游戏
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-12 16:58:38
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-12 17:19:19
'''
'''
Craps赌博游戏：
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
'''

from random import randint

money = 1000
while money > 0:
    print("你的资产: %d" % money)
    need_continue = False
    while True:
        bet = int(input("请下注："))
        if bet > 0 and bet <= money:
            break
    first = randint(1,6) + randint(1,6)
    print("你掷出了 %d 点" % first)
    if first == 7 or first == 11:
        money += bet
        print("你赢了！ 你的资产： %d " % money)
    elif first == 2 or first == 3 or first == 12:
        money -= bet
        print("庄家胜！ 你的资产： %d " % money)
    else:
        need_continue = True
    
    while need_continue:
        current = randint(1,6) + randint(1,6)
        print("你掷出了 %d 点" % current)
        if current == 7:
            money -= bet
            print("庄家胜！ 你的资产： %d " % money)
            need_continue = False
        elif current == first:
            money += bet
            print("你赢了！ 你的资产： %d " % money)
            need_continue = False
else:
    print("You are Break ! Fuck off !")