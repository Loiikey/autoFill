import selenium
import re
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# url = "https://www.wjx.cn/vm/OFwyNxu.aspx"
url = "https://www.wjx.cn/vm/OFwyNxu.aspx"

className = "field.ui-field-contain"

def Pass():
    op = webdriver.EdgeOptions()
    op.add_experimental_option('detach',True)
    # op.add_argument('--headless')
    # op.add_experimental_option('excludeSwitches', ['enable-automation'])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("disable-blink-features=AutomationControlled")
    # op.add_argument("--proxy-server={}.{}.{}.{}:{}".format(114,55,225,14,80))
    return op
def openUrl(url):
    """ 打开问卷并且返回driver """
    op = Pass()
    driver = webdriver.Edge(options=op)
    driver.get(url)
    return driver

def close(driver):
    """ 关闭网页(driver) """
    driver.close()


path = '//*[@id="div1"]/div[2]/div[1]/span/a'
def aXpath(divId,opId):
    return '//*[@id="'+ str(divId) + '"]/div[2]/div['+ str(opId) +']/span/a'
def opXpath(divId,opId):
    return '//*[@id="'+ str(divId) + '"]/div[2]/div['+ str(opId) +']'


def radio(divId,element):
    xpath = '//*[@id="'+divId+'"]/div[2]'
    sons = element.find_element(By.XPATH,xpath)
    number = len(sons.find_elements(By.XPATH,'./*'))
    finalXpath = opXpath(divId,number)
    finalElement = sons.find_element(By.XPATH,finalXpath)
    x = len(finalElement.find_elements(By.XPATH,'./*'))
    if x == 3:
        number -= 1
    opId = random.randint(1,number)
    a = element.find_element(By.XPATH,aXpath(divId,opId))
    a.click()
def checkbox(divId,element):
    maxValue = element.get_attribute("maxvalue")
    if maxValue is None:
        maxValue = 0
    maxValue = int(maxValue)
    sons = element.find_element(By.CLASS_NAME,"ui-controlgroup.column1")
    number = len(sons.find_elements(By.XPATH,'./*'))
    finalXpath = opXpath(id,number)
    finalElement = sons.find_element(By.XPATH,finalXpath)
    x = len(finalElement.find_elements(By.XPATH,'./*'))
    if x == 3:
        number -= 1
        maxValue -= 1
    number = max(maxValue,number)
    ls = random.sample(range(1,number+1),random.randint(1,number))
    for i in ls:
        a = element.find_element(By.XPATH,aXpath(divId,i))
        a.click()
def rowtile(divId,element):
    rowXpath = '//*[@id="div'+str(divId)+'"]/div[2]'
    id = "divRefTab" + str(divId)
    txpth = '//*[@id="'+id+'"]/tbody'
    rowElement = element.find_element(By.XPATH,rowXpath).find_element(By.ID,id).find_element(By.XPATH,txpth)
    number = len(rowElement.find_elements(By.TAG_NAME,"tr"))//2
    num = 0
    for i in range(1,number+1):
        colxpath = '//*[@id="drv'+str(divId)+'_'+str(i)+'"]'
        colElement = rowElement.find_element(By.XPATH,colxpath)
        if num == 0:
            num = len(colElement.find_elements(By.TAG_NAME,"a"))
        randomNum = random.randint(1,num)
        axpth = colxpath + '/td[' + str(randomNum+1) + ']'
        el = colElement.find_element(By.XPATH,axpth)
        el.click()

def start():
    pass
if __name__ == '__main__':
    n = 1
    per = 1
    while n > 0:
        driver = openUrl(url)
        all = driver.find_element(By.XPATH,'//*[@id="fieldset1"]')
        allnum = len(all.find_elements(By.XPATH,'./*')) 
        for i in range(1,allnum+1):
            id = "div" + str(i) + ""
            try:
                element = driver.find_element(By.ID,id)
            except:
                pass
            typeId = int(element.get_attribute("type"))
            if typeId == 3:
                radio(id,element)
            elif typeId == 4:
                checkbox(id,element)
            elif typeId == 6:
                rowtile(i,element)
        try:
            driver.find_element(By.XPATH,'//*[@id="rectTop"]').click()
        except:
            pass
        driver.find_element(By.ID,"ctlNext").click()
        close(driver)
        n -= 1
        
        print('========= 当前是第 ',per,' 次 ==========')
        per += 1
        time.sleep(0.5)
    print(" ============== 程序终止 ==============")
    pass
