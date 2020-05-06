'''
@Description: 
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-03-16 11:53:00
@LastEditors: CornC.fcx
@LastEditTime: 2020-04-07 15:34:45
'''

import os, re
import xlrd, xlwt
from xlutils.copy import copy
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines

def getInfoFromPdf(filepath):
    try:
        fp = open(filepath, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument(parser)
        fileName = os.path.basename(filepath)
        print(fileName)

        companyInfo = [fileName]

        if doc.is_extractable:
            #创建一个PDF资源管理器对象来存储共享资源,caching = False不缓存
            pdfrm = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(pdfrm, laparams=laparams)
            #创建一个PDF解析器对象
            interpreter = PDFPageInterpreter(pdfrm, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if hasattr(x, "get_text"):
                        content = x.get_text()
                        if content.find('送检单位：') > -1:
                            tempInfo = content.split('：')[1]
                            companyName = tempInfo.split('\n')[0]
                            companyInfo.append(companyName.strip())
                        if content.find('人') > -1:
                            humanSum = content.split(' ')[0]
                            if re.match(r'\d', humanSum):
                                companyInfo.append(humanSum)
                        if content.find('收样时间：') > -1:
                            tempInfo = content.split('：')[1]
                            sampleDate = tempInfo.split('\n')[0]
                            companyInfo.append(sampleDate.strip())
        print(companyInfo)
        writeLine('test2.xlsx', companyInfo)
        return companyInfo
    except Exception as e:
        print("Exception:%s",e)

def getAllFileInfos(filesDir):
    infoList = []
    files = os.listdir(filesDir)
    for file in files:
        fileSuffix = os.path.splitext(file)[1]
        if fileSuffix == '.pdf':
            fileInfo = getInfoFromPdf(filesDir + '\\' + file)
            infoList.append(fileInfo)

    return infoList

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

def writeLine(filePath, info):

    workbook = xlrd.open_workbook(filePath)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for j in range(0, len(info)):
        new_worksheet.write(rows_old, j, info[j])
    new_workbook.save(filePath)

if __name__ == '__main__':
    # D:\需要处理\全集
    # D:\Program Files\GitHubRepositories\BasicLearning\PythonLearing\Python_Corn\20200313
    infoList = getAllFileInfos(r'C:\Users\dell\Desktop\3.15')
    # writeExcel('test2.xlsx', infoList)