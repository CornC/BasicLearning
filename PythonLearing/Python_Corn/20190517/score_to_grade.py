'''
@Description: 百分之分数转化成等级
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 17:06:28
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 17:13:32
'''

'''
score > 90        -------> A
80 < score <= 90  -------> B
60 < score <= 80  -------> C
score < 60        -------> D 
'''

score = int(input('Input Score (100) : '))
if score > 90:
    grade = 'A'
elif score > 80 and score <= 90:
    grade = 'B'
elif score > 60 and score <= 80:
    grade = 'C'
else:
    grade = 'D'

print('You Grade is ', grade)