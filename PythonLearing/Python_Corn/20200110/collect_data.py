'''
@Description: 整理收集的数据
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-01-10 09:10:37
@LastEditors: CornC.fcx
@LastEditTime: 2020-03-16 13:01:08
'''

import xlrd
import xlwt
import os
from xlutils.copy import copy


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿

def read_excel_xls(path, column):
    work_data = []
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(1, worksheet.nrows):
        row_data = column
        for j in range(0, worksheet.ncols):
            row_data = [worksheet.cell_value(i, j) if worksheet.cell_value(0, j) == x else x for x in row_data]
            # row_data.append(worksheet.cell_value(i, j))
            # 按列再排序

        work_data.append(row_data)
    return work_data

def get_all_path(folder_path):
    path_list = []
    fileList = os.listdir(folder_path)  # 列出文件夹下所有的目录与文件
    for fileName in fileList:
        if os.path.splitext(fileName)[1] == '.xlsx':
            path_list.append(folder_path + '\\' + fileName)
    return path_list

if __name__ == "__main__":

    column_names = ['Sample_ID','rs10875943','rs10936632','rs12653946','rs13385191','rs1447295','rs17401966','rs1983891','rs2596542','rs339331','rs36600','rs4488809','rs753955','rs9275572','rs9600079']

    folder_path = r'C:\Users\dell\Desktop\女肿\数据\Result\AC-03'
    result_file_path = r'C:\Users\dell\Desktop\女肿\数据\AC-03_Result.xlsx'
    filePathList = get_all_path(folder_path)
    # print(filePathList)
    for path in filePathList:
        file_data = read_excel_xls(path,column_names)
        write_excel_xls_append(result_file_path, file_data)

    print('写入完成！')