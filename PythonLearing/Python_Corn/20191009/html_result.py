'''
@Description: 向网页内填充内容 获取网页返回的数据
@version: v1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-10-09 11:25:35
@LastEditors: CornC.fcx
@LastEditTime: 2019-11-01 11:09:32
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
import time
import sys  #引入模块

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):
    url = "https://fetalmedicine.org/research/assess/preeclampsia/first-trimester"
    driver.get(url)

    # 选择
    Select(driver.find_element_by_id("CalculatorPeMom_twins")).select_by_visible_text('Singleton')
    Select(driver.find_element_by_id("CalculatorPeMom_race")).select_by_visible_text('East Asian')
    Select(driver.find_element_by_id("CalculatorPeMom_conception")).select_by_visible_text('Spontaneous')

    # 找到输入框并输入查询内容
    Crown_Rump_length = driver.find_element_by_id("CalculatorPeMom_crl1")
    Crown_Rump_length.send_keys("67")

    Examination_date = driver.find_element_by_id("CalculatorPeMom_ga_at")
    Examination_date.send_keys("11-04-2019")

    Birthday = driver.find_element_by_id("CalculatorPeMom_dob")
    Birthday.send_keys("01-01-1982")

    Height = driver.find_element_by_id("CalculatorPeMom_height")
    Height.send_keys("160")

    Weight = driver.find_element_by_id("CalculatorPeMom_weight")
    Weight.send_keys("53")

    MAP = driver.find_element_by_id("CalculatorPeMom_map")
    MAP.send_keys("83.33")

    TestDate = driver.find_element_by_id("CalculatorPeMom_biophysical_at")
    TestDate.send_keys("11-04-2019")

    # 处理　radio
    # IsSmoking = driver.find_element_by_id("CalculatorPeMom_smoking_1")
    IsSmoking = driver.find_element_by_id("CalculatorPeMom_smoking_1")
    IsSmoking.click()
    # IsSmoking.find_element_by_xpath("//input[@value='2']").click()
    # IsSmoking.click()

    # IsMotherPatient = driver.find_element_by_id("CalculatorPeMom_mother_pe")
    IsMotherPatient = driver.find_element_by_id("CalculatorPeMom_mother_pe_1")
    IsMotherPatient.click()
    # IsMotherPatient.find_element_by_xpath("//input[@value='2']").click()
    # IsMotherPatient.click()
    
    # Chronic_hypertension = driver.find_element_by_id("CalculatorPeMom_chronic_hypertension")
    Chronic_hypertension = driver.find_element_by_id("CalculatorPeMom_chronic_hypertension_1")
    Chronic_hypertension.click()
    # Chronic_hypertension.find_element_by_xpath("//input[@value='2']").click()
    # CalculatorPeMom_smoking_1
    # Chronic_hypertension.click()

    # Diabetes_1 = driver.find_element_by_id("CalculatorPeMom_diabetes_type_i")
    Diabetes_1 = driver.find_element_by_id("CalculatorPeMom_diabetes_type_i_1")
    Diabetes_1.click()
    # Diabetes_1.find_element_by_xpath("//input[@value='0']").click()
    # CalculatorPeMom_smoking_1
    # Diabetes_1.click()

    # Diabetes_2 = driver.find_element_by_id("CalculatorPeMom_diabetes_type_ii_1")
    Diabetes_2 = driver.find_element_by_id("CalculatorPeMom_diabetes_type_ii_1")
    Diabetes_2.click()
    # Diabetes_2.find_element_by_xpath("//input[@value='0']").click()
    # CalculatorPeMom_smoking_1
    # Diabetes_2.click()

    # SLE = driver.find_element_by_id("CalculatorPeMom_sle")
    SLE = driver.find_element_by_id("CalculatorPeMom_sle_1")
    SLE.click()
    # SLE.find_element_by_xpath("//input[@value='0']").click()
    # CalculatorPeMom_smoking_1
    # SLE.click()

    # Previous = driver.find_element_by_id("CalculatorPeMom_previous_0")
    Previous = driver.find_element_by_id("CalculatorPeMom_previous_0")
    Previous.click()
    # Previous.find_element_by_xpath("//input[@value='0']").click()
    # CalculatorPeMom_smoking_1
    # Previous.click()

    # APS = driver.find_element_by_id("CalculatorPeMom_aps_1")
    APS = driver.find_element_by_id("CalculatorPeMom_aps_1")
    APS.click()
    # APS.find_element_by_xpath("//input[@value='0']").click()
    # APS.click()

    RawData = driver.find_element_by_id("CalculatorPeMom_include_plgf_2")
    RawData.click()

    time.sleep(2)

    plgfData = driver.find_element_by_id("CalculatorPeMom_plgf")
    plgfData.send_keys("12.1")

    Select(driver.find_element_by_id("CalculatorPeMom_plgf_machine")).select_by_visible_text('Delfia')

    measureDate = driver.find_element_by_id("CalculatorPeMom_biochemical_at")
    measureDate.send_keys("11-04-2019")
    # 提交表单
    driver.find_element_by_xpath("//*[@value='Calculate risk']").click()

    MAP1 =  driver.find_element_by_xpath("//div[@class='col-xs-12'][1]").text
    MAP_MoM = driver.find_element_by_xpath("//div[@class='col-xs-12'][1]/span").text

    PLGF =  driver.find_element_by_xpath("//div[@class='col-xs-12'][2]").text

    RiskValue = driver.find_element_by_xpath("//div[@class='markers']/table/tbody/tr/td[1]").text + driver.find_element_by_xpath("//div[@class='markers']/table/tbody/tr/td[2]").text
    
    print(RiskValue)
    print(MAP_MoM)
    print(MAP1)
    print(PLGF)


    print('查询操作完毕！')

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    args1 = sys.argv[1]
    args2 = sys.argv[2]

    print(args1)
    print(args2)

    driver = openChrome()
    operationAuth(driver)
    driver.close()