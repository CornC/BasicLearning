'''
@Description: 删除PDF中的Logo
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-03-25 09:08:28
@LastEditors: CornC.fcx
@LastEditTime: 2020-03-25 16:46:27
'''

'''
直接修改 PDF 内容不太现实
参考网上的资源 现尝试使用一个比较有意思且有实现可能性的方法来删除文件 Logo
具体实现步骤如下：
    1. 将 PDF 文件拆分为单个 PDF 文件
    2. 将拆分好的单个 PDF 文件转成图片格式
    3. 使用图片处理方法 分割图片 之后合成新图片
    4. 将图片转为单个 PDF 文件 最后合并
'''

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from wand.image import Image as wandImage


class Del_Logo(object):

    def __init__(self):   
        # 具体需要的几个参数

        # 源 PDF 文件名
        self.pdf_name = "delLogo_1.pdf"
        # 新 PDF 文件名
        self.newPdf_name = "New_1.pdf"
        # PDF 文件总页数
        self.pdf_totalPages = 0
        # 图片文件后缀
        self.image_suffix = ".png"
        # 图片文件精度（dpi）
        self.image_resolution = 220
        # 图片的属性

        # 图片
        self.loc_left = 0
        self.loc_top = 200
        self.width = 1819
        self.height = 2572

        print("Init Values!")

    # 方法总入口
    def run(self):
        
        self.split_Pdf(self.pdf_name)

        for i in range(self.pdf_totalPages):
            pdfFileName = './tmp/' + str(i) + '.pdf'
            imageFileName = './tmp/' + str(i) + self.image_suffix
            self.pdf_to_image(pdfFileName, imageFileName, self.image_resolution)

        for i in range(self.pdf_totalPages):
            oldImgName = './tmp/' + str(i) + self.image_suffix
            newImgName = './tmp/' + str(i) + '_new' + self.image_suffix
            self.imgHandler(oldImgName, newImgName, self.loc_left, self.loc_top, self.width, self.height)

        for i in range(self.pdf_totalPages):
            pdfName = './tmp/' + str(i) + "_new.pdf"
            imgName = './tmp/' + str(i) + '_new' + self.image_suffix
            self.image_to_pdf(imgName, pdfName)
        
        fileList = []
        for i in range(self.pdf_totalPages):
            pdfName = './tmp/' + str(i) + "_new.pdf"
            fileList.append(pdfName)

        self.merge_pdf(fileList, self.newPdf_name)
        print("操作完成！")
        return
    # 拆分文件
    def split_Pdf(self, fileName):
        
        print("拆分文件！")
        pdfReader = PdfFileReader(open(fileName, 'rb'))
        pageCount = pdfReader.getNumPages()

        self.pdf_totalPages = pageCount
        print("文件总页数： ", self.pdf_totalPages)

        # 将 PDF 文件拆分成单个文件
        for pageIndex in range(self.pdf_totalPages):
            page = pdfReader.getPage(pageIndex)
            pdfwriter = PdfFileWriter()
            pdfwriter.addPage(page)
            writeFileName = "./tmp/" + str(pageIndex) + ".pdf"

            pdfwriter.write(open(writeFileName, 'wb'))
    
    # PDF 文件转为 PNG 图片
    def pdf_to_image(self, FileName, ImageName, ImageResolution):

        with wandImage(filename=FileName, resolution=ImageResolution) as img:
            with img.convert('png') as converted:
                converted.save(filename=ImageName)

        print("Pdf to Image:", FileName, ImageName)

    # 处理图片
    def imgHandler(self, ImageName, newImgName, loc_x, loc_y, width, height):

        img = Image.open(ImageName, mode='r')
        region = img.crop((loc_x, loc_y, loc_x + width, height))
        region.save(newImgName)

        # 设置新的图片
        im = Image.open(newImgName).convert("RGBA")
        x, y = im.size
        p = Image.new('RGBA', (width, height), (255,255,255))
        p.paste(im, (0, loc_y, x, loc_y + y), im)
        p.save(newImgName)

    # PNG 图片转为 PDF 文件
    def image_to_pdf(self, ImageName, PdfName):

        # im_list = []
        img = Image.open(ImageName)
        (maxWidth, maxHeight) = img.size
        c = canvas.Canvas(PdfName, pagesize=portrait((maxWidth, maxHeight)))
        c.drawImage(ImageName, 0, 0, maxWidth, maxHeight)
        c.showPage()
        c.save()
        # if img.mode == "RGBA":
        #     img = img.convert('RGB')
        #     im_list.append(img)
        
        # img.save(PdfName, "PDF", resolution=100.0, save_all=True, append_images=im_list)
        print("Pdf to Image:", PdfName, ImageName)
    
    # 合并单页 PDF
    def merge_pdf(self, fileList, outFile):
        print("合成 PDF")
        pdf_out = PdfFileWriter()
        for file in fileList:
            pdfInfo = PdfFileReader(open(file, 'rb'))
            page_count = pdfInfo.getNumPages()

            for i in range(page_count):
                pdf_out.addPage(pdfInfo.getPage(i))

        pdf_out.write(open(outFile, 'wb'))

if __name__ == "__main__":

    delLogo = Del_Logo()
    delLogo.run()