'''
@Description: 一些简单的文件操作的练习
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-12 15:01:00
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-12 15:55:51
'''

'''
| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |
'''

'''
    encoding 指定编码 不指定时采用系统默认的编码
'''
def readFile():
    f = open('test.txt', 'r', encoding='utf-8')
    # 一次将全部文件内容都出来
    print(f.read())

    # 一次读一行数据
    for line in f:
        print(line, end=' ')

    # 读取文件存储到列表中
    f.readlines()

    # 文件流记得要关闭
    f.close()

# 为了代码的健壮性，需要在程序出错时拦截错误，保证不会因此崩溃

def handleError():
    f = None
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('找不到文件！')
    except LookupError:
        print('未知编码！ ')
    except UnicodeDecodeError:
        print('解码错误！ ')
    finally:
        if f:
            f.close()

# 上面的另一种写法，可以免掉关闭文件流的操作

def read():
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

# 写文件

def WriteFile():
    # 覆盖写入 'w' 文尾新增 'a'
    f = None
    try:
        f = open('test.txt', 'a', encoding='utf-8') 
        f.write()
    except IOError as ex:
        print(ex)
        print('Error !')
    finally:
        if f:
            f.close()

# 二进制文件的处理

def handel_binary():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('读写文件时出现错误.')
    print('程序执行结束.')

# JSON 文件的处理

'''
    - `dump` - 将Python对象按照JSON格式序列化到文件中
    - `dumps` - 将Python对象处理成JSON格式的字符串
    - `load` - 将文件中的JSON数据反序列化成对象
    - `loads` - 将字符串的内容反序列化成Python对象
'''

if __name__ == '__main__':
    readFile()
