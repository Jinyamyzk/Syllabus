import time
from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
import csv

def score_to_gpa(score):
    if score == '秀':
        return 4.2
    elif score == '優':
        return 4
    elif score == '良':
        return 3
    elif score == '可':
        return 2
    elif score == '不可':
        return 0
    elif score == '合格':
        return 2
    elif score == '取消':
        return 0

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
time.sleep(1)

to_top = driver.find_element_by_xpath("/html/body/div/form/input[8]")
to_top.click()
time.sleep(1)
to_tanni = driver.find_element_by_css_selector("#wf_PTW0005001-s_20120920145156-UsualMenuForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > a")
to_tanni.click()
time.sleep(1)
driver.switch_to_frame(driver.find_element_by_css_selector("#main-frame-if"))
hyouji = driver.find_element_by_css_selector("#rishuSeisekiReferListForm > table > tfoot > tr > td > input:nth-child(1)")
hyouji.click()
#
time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
tbody= soup.select('body > table.normal > tbody')
tr_tags = tbody[0].find_all('tr')

grades = []

for tr_tag in tr_tags:
    list = []
    td_tags = tr_tag.find_all('td')
    if td_tags[4].text.strip() == '履修取消':
        continue
    list.append(td_tags[4].text.strip())
    list.append(td_tags[1].text.strip())
    gpa = score_to_gpa(td_tags[6].text.strip())
    list.append(gpa)
    grades.append(list)

with open('/Users/Jinya/Desktop/Syllabus/grade.csv', 'w',encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(["年度","時間割コード","GPA"])
        writer.writerows(grades)



time.sleep(3)
driver.quit()
