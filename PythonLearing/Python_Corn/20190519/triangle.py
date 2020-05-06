'''
@Description: 画出不同的三角形
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-20 14:19:37
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-21 11:53:12
'''

'''
*
**
***
****
*****
   
    *   
   **
  ***
 ****
*****

    *   
   ***  
  ***** 
 *******
*********
'''

'''
row = int(input('Input Row Count : '))
'''

for i in range(5):
    for _ in range(i+1):
        print('*', end = '')
    print()


for i in range(5):
    for j in range(5):
        if j < 5 - i - 1:
            print('-', end = '')
        else:
            print('*', end = '')
    print()

# for i in range(6):
#     for j in range(6-i):
#         print('-', end = '')
#     for k in range(6+i-j):
#         print('*', end = '')
#     print()       

for i in range(6):
    for j in range(6-i-1):
        print('-', end = '')
    for k in range(2*i+1):
        print('*', end = '')
    print()    