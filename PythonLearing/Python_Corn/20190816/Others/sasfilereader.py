'''
@Description: 读取 sas7bdat 文件
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-09-16 10:20:42
@LastEditors: CornC.fcx
@LastEditTime: 2019-09-16 10:26:34
'''

from sas7bdat import SAS7BDAT
f = SAS7BDAT(r'loc_risk_score_per_sample.sas7bdat', encoding="gb2312").to_data_frame()