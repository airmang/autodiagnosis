import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

password = '4988'

driver = webdriver.Chrome()
url_path = 'https://hcs.eduro.go.kr/#/loginWithUserInfo'
driver.get(url_path)
driver.implicitly_wait(5)
driver.maximize_window()

login_button1 = driver.find_element(By.CLASS_NAME, 'loginHome_typeCheck.type1').click()

login_button2 = driver.find_element(By.ID, "btnConfirm2").click()

driver.implicitly_wait(5)
find_button1 = driver.find_element(By.CLASS_NAME, "searchBtn").click()
select_sido = Select(driver.find_element(By.ID, "sidolabel"))
select_sido.select_by_value('10')
select_sc = Select(driver.find_element(By.ID, "crseScCode"))
select_sc.select_by_value('3')

schoolname = driver.find_element(By.CLASS_NAME, "searchArea")
schoolname.send_keys('안산부곡중학교')
schoolname.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

selectedSchool = driver.find_element(By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p').click()
select_button = driver.find_element(By.CLASS_NAME, "layerFullBtn").click()

name = driver.find_element(By.ID, "user_name_input")
name.send_keys('고규현')
birth = driver.find_element(By.ID, "birthday_input")
birth.send_keys('931108')
confirm_button = driver.find_element(By.ID, "btnConfirm").click()
driver.implicitly_wait(20)
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()

keys = []

inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[4]/a')
label_num = inputkey.get_attribute("aria-label")
keys.append(label_num)
for x in range(1, 5):
    inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[5]/a['+str(x)+']')
    label_num = inputkey.get_attribute("aria-label")
    keys.append(label_num)

inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[6]/a')
label_num = inputkey.get_attribute("aria-label")
keys.append(label_num)

inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[7]/a')
label_num = inputkey.get_attribute("aria-label")
keys.append(label_num)
for x in range(1, 5):
    inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[8]/a['+str(x)+']')
    label_num = inputkey.get_attribute("aria-label")
    keys.append(label_num)

inputkey = driver.find_element(By.XPATH, '//*[@id="password_mainDiv"]/div[9]/a')
label_num = inputkey.get_attribute("aria-label")
keys.append(label_num)

inputkeys = ['//*[@id="password_mainDiv"]/div[4]/a', '//*[@id="password_mainDiv"]/div[5]/a[1]', '//*[@id="password_mainDiv"]/div[5]/a[2]', '//*[@id="password_mainDiv"]/div[5]/a[3]', '//*[@id="password_mainDiv"]/div[5]/a[4]','//*[@id="password_mainDiv"]/div[6]/a', '//*[@id="password_mainDiv"]/div[7]/a', '//*[@id="password_mainDiv"]/div[8]/a[1]', '//*[@id="password_mainDiv"]/div[8]/a[2]', '//*[@id="password_mainDiv"]/div[8]/a[3]', '//*[@id="password_mainDiv"]/div[8]/a[4]', '//*[@id="password_mainDiv"]/div[9]/a']

for Pass in password:
    if Pass == "\n":
        pass
    else:
        index = keys.index(Pass)
        driver.find_element(By.XPATH, inputkeys[index]).click()
        time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="survey_q1a1"]').click()
driver.find_element(By.XPATH, '//*[@id="survey_q2a3"]').click()
driver.find_element(By.XPATH, '//*[@id="survey_q3a1"]').click()

driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click()