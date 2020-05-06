'''
@Description: 
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-03-13 13:09:52
@LastEditors: CornC.fcx
@LastEditTime: 2020-05-06 11:04:54
'''

import os
import time
import shutil

def findFilesInDir(fileDir, targetDir):
    for rootPath, dirPath, files in os.walk(fileDir):  
        targetTimeStr = "2020-03-09 12:00:00"
        targetTime = time.strptime(targetTimeStr, "%Y-%m-%d %H:%M:%S")
        for file in files:
            full_path = os.path.join(rootPath, file)
            file_modify_time_value = os.stat(full_path).st_mtime
            file_modify_time = time.localtime(file_modify_time_value)
            print(file_modify_time)
            if file_modify_time > targetTime:
                shutil.copy(full_path, targetDir)

def getFilesInDir(fileDir, targetDir):
    for rootPath, dirPath, files in os.walk(fileDir):  
        print(dirPath)
        targetNameList = ['测试1', '测试2', '测试3', '测试4']

        for name in targetNameList:
            filePathList = []
            for file in files:
                full_path = os.path.join(rootPath, file)
                if file.find(name) != -1:
                    filePathList.append(full_path)

            if len(filePathList) > 1: # 创建文件夹
                if os.path.exists(targetDir + '\\' + name):
                    for f in filePathList:
                        shutil.copy(f, targetDir + '\\' + name)
                else:
                    os.makedirs(targetDir + '\\' + name)
                    for f in filePathList:
                        shutil.copy(f, targetDir + '\\' + name)
            else:
                shutil.copy(filePathList[0], targetDir)

if __name__ == "__main__":
    findFilesInDir(r'C:\Users\dell\Desktop\fileDir', r'C:\Users\dell\Desktop\tarDir')