'''
@Description: 
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-03-17 14:33:21
@LastEditors: CornC.fcx
@LastEditTime: 2020-03-23 09:22:46
'''

import tabula
import os
import xlrd
import xlwt
from xlutils.copy import copy


def getAllFileInfos(filesDir):
    files = os.listdir(filesDir)
    for file in files:
        print(file)
        fileSuffix = os.path.splitext(file)[1]
        if fileSuffix == '.pdf':
            getTableInfo(filesDir + '\\' + file)

def getTableInfo(filepath=''):
    df = tabula.read_pdf(r'test3.pdf', encoding='gbk', pages='all', multiple_tables=True)
    print(df)
    fileInfo = []
    for i in df.index:
        # 遍历打印企业名称
        fileInfo.append(df.loc[i].values)
    print(fileInfo)
    # writeExcel('团检信息.xlsx', fileInfo)
    # tabula.convert_into("test1.pdf", "output.csv", output_format="csv", pages='all')

def writeExcel(filePath, infoList):

    index = len(infoList)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(filePath)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(infoList[i])):
            new_worksheet.write(i + rows_old, j, infoList[i][j])
    new_workbook.save(filePath)

def getAllInfo(filesDir):
    tabula.convert_into_by_batch(filesDir, output_format = "csv", pages = "all", multiple_tables=True)

if __name__ == "__main__":
    getAllInfo(r'D:\需要处理\缺少的文件')
    # getAllFileInfos(r'D:\需要处理\全集')