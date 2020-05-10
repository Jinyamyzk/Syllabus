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


driver.find_element_by_id('j_username').send_keys('1686592c')#自分のIDを入れる
driver.find_element_by_id('j_password').send_keys('IY30q4Ef')#パスワードを入れる
driver.find_element_by_name('_eventId_proceed').click()
print('ログイン成功')
time.sleep(3)

to_top = driver.find_element_by_xpath("/html/body/div/form/input[8]")
print(to_top)
to_top.click()
time.sleep(3)
to_tanni = driver.find_element_by_xpath("/html/body/div[3]/div[2]/table/tbody/tr[4]/td[1]/div/div[3]/div[2]/div/form/table/tbody/tr[4]/td[2]/div/a")
to_tanni.click()
time.sleep(5)
hyouji = driver.find_element_by_css_selector("#taniReferListForm > table > tfoot > tr > td > input:nth-child(1)")
hyouji.click()

time.sleep(3)

driver.quit()
