'''
@Description: 分段函数求解
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 16:15:00
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 16:43:04
'''
'''
                            3x - 5 (x > 1)
function piecewise(x) =     x + 2  (-1 <= x <= 1)
                            5x + 3 (x < -1)
'''

param = float(input('Input Param : '))

if param > 1:
    y = 3 * param - 5
elif param >= -1 and param <= 1:
    y = param + 2
else:   
    y = 5 * param + 3

print(' y = %.2f' % (y))
