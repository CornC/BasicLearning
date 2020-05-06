'''
@Description: 练习
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-01 15:46:09
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-07 16:28:24
'''

#  跑马灯
import os
import time
import random


def carousel():

    content = '只是刚好情窦初开遇到你···'

    while True:

        os.system('cls')
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]


# 生成任意数量的验证码


def generate_code(code_len=4):

    all_code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_code) - 1
    code = ''

    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_code[index]
    return code


# 获取文件后缀名


def get_suffix(fileName, find_dot=False):

    dot_pos = fileName.rfind('.')
    if 0 < dot_pos < len(fileName) - 1:
        index = dot_pos if find_dot else dot_pos + 1
        return fileName[index:]
    else:
        return None


# 判断某年某月某日是第几天


# 判断是否是闰年
def is_leap(year):

    return year % 4 == 0 and year % 10 != 0 and year % 400 == 0


# 判断前几个月的累加日期在加上当天日期
def which_day(year, month, day):

    month_days = [[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,
                   31]][is_leap(year)]

    total = 0
    for index in range(month - 1):
        total += month_days[index]
    return total + day


# 杨辉三角

def yang_triangle(rows):
    yh = [[]] * rows
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


# 双色球

from random import randint, sample

# sample(a, n) 是从序列 a 中随机抽取 n 个元素并以 list 形式返回

def select_balls():

    red_balls = [x for x in range(1,34)]
    select_balls = []
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1,16))
    return select_balls

def display_result(balls):

    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end = ' ')
        print('%02d' % ball, end=' ')
    print()

def get_start(n = 3):

    for _ in range(n):
        display_result(select_balls())

# 约瑟夫问题

def josephus_problem(n = 30, m = 4):

    persons = [True] * n
    
    count, index, number = 0, 0, 0
    while count < n:
        if persons[index]:
            number += 1
            if number == m:
                persons[index] = False
                count += 1
                number = 0
                print('%d' % index, end = ' ')
        index += 1
        index %= n

# 井字棋

import os

# 绘制棋盘
def print_board(board):
    print(board['LT'] + ' | ' + board['CT'] + ' | ' + board['RT'])
    print('--+---+--')
    print(board['LC'] + ' | ' + board['CC'] + ' | ' + board['RC'])
    print('--+---+--')
    print(board['LB'] + ' | ' + board['CB'] + ' | ' + board['RB']) 

# 下棋
def play_chess():

    init_board = {
        'LT': ' ', 'CT': ' ', 'RT': ' ',
        'LC': ' ', 'CC': ' ', 'RC': ' ',
        'LB': ' ', 'CB': ' ', 'RB': ' '
    }
    begin = True
    while begin:
        current_board = init_board.copy()
        begin = False
        os.system('cls')
        turn = 'X'
        counter = 0
        print_board(init_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if current_board[move] == ' ':
                counter += 1
                current_board[move] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            os.system('cls')
            print_board(current_board)
        # if init_board['LT'] == init_board['CT'] == init_board['RT'] != ' ' or init_board['LC'] == init_board['CC'] == init_board['RC'] != ' ' or init_board['LB'] == init_board['CB'] == init_board['RB'] != ' '\
        #     or init_board['LT'] == init_board['CC'] == init_board['RB'] != ' ' or init_board['LB'] == init_board['CC'] == init_board['RT'] != ' ' or init_board['LT'] == init_board['LC'] == init_board['LB'] != ' '\
        #     or init_board['CT'] == init_board['CC'] == init_board['CB'] != ' ' or init_board['RT'] == init_board['RC'] == init_board['RB'] != ' ':
        #     print('GAME OVER!')
        #     break
        choice = input('Another Game? (Y|N)')
        begin = choice == 'y' or choice == 'Y'

    

if __name__ == '__main__':
    # carousel()
    # print(generate_code())
    # print(generate_code(6))
    # print(get_suffix('sadasdas.txt'))
    # print(which_day(2019, 8, 2))
    # print(yang_triangle(4))
    # get_start(5)
    # josephus_problem(6, 5)
    play_chess()