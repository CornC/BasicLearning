'''
@Description: 将pdf文件从一个文件夹里提取出来
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-04-07 13:41:31
@LastEditors: CornC.fcx
@LastEditTime: 2020-04-07 13:57:45
'''

import os
import shutil

def getFiles(fileDir, tarDir=''):
    fileInfoList = []
    for rootPath, dirPath, files in os.walk(fileDir):
        for file in files:
            fileSuffix = os.path.splitext(file)[1]
            if fileSuffix == '.pdf':
                full_path = os.path.join(rootPath, file)
                fileInfoList.append(full_path + '\n')
                shutil.copy(full_path, tarDir)

    with open('PdfPath.txt', 'w') as f:
        f.writelines(fileInfoList)

if __name__ == "__main__":
    getFiles(r'E:\数据文件\检测部3月15后报告', r'C:\Users\dell\Desktop\3.15')
    