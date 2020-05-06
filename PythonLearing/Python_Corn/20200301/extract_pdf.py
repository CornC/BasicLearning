'''
@Description: 从pdf中提取信息
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-03-01 10:35:04
@LastEditors: CornC.fcx
@LastEditTime: 2020-03-16 11:59:56
'''

import os,re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def pdfTotxt(filepath, outpath):
    try:
        fp = open(filepath, 'rb')
        outfp=open(outpath, 'w')
        #创建一个PDF资源管理器对象来存储共享资源,caching = False不缓存
        rsrcmgr = PDFResourceManager(caching = False)
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=laparams,imagewriter=None)
        #创建一个PDF解析器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos = set(),maxpages=0,
                                      password='',caching=False, check_extractable=True):
            page.rotate = page.rotate % 360
            interpreter.process_page(page)
        #关闭输入流
        fp.close()
        #关闭输出流
        device.close()
        outfp.flush()
        outfp.close()
    except Exception as e:
        print("Exception:%s",e)

def fileTotxt(fileDir):
    files=os.listdir(fileDir)
    tarDir=fileDir+'txt'
    if not os.path.exists(tarDir):
        os.mkdir(tarDir)
    replace=re.compile(r'\.pdf',re.I)
    for file in files:
        filePath=fileDir+'\\'+file
        outPath=tarDir+'\\'+re.sub(replace,'',file)+'.txt'
        pdfTotxt(filePath,outPath)
        print("Saved "+outPath)

if __name__ == '__main__':
    pdfTotxt(u'test1.pdf', 'test1.txt')
    # fileTotxt('这里是目录的路径')
