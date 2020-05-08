import time
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()




url = 'http://www.office.kobe-u.ac.jp/stdnt-kymsys/student/student.html'
driver.get(url)
time.sleep(1)
element = driver.find_element_by_css_selector("#uribo_net > h2 > a > img")
element.click()
time.sleep(1)


driver.find_element_by_id('j_username').send_keys('')#自分のIDを入れる
driver.find_element_by_id('j_password').send_keys('IY30q4Ef')#パスワードを入れる
driver.find_element_by_name('_eventId_proceed').click()
print('ログイン成功')
