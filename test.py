import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import chromedriver_binary
from bs4 import BeautifulSoup
import requests
import csv
from janome.tokenizer import Tokenizer


def add_sum_class(nendo):
    soup = BeautifulSoup(page_source, 'html.parser')

    #tr_tagを取得
    table = soup.select_one('table.normal')
    tbody = table.select_one('tbody')
    tr_tags = tbody.select('tr')



    i=0
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all('td')
        print(td_tags[7])
        syllabus_url = "https://kym-syllabus.ofc.kobe-u.ac.jp/kobe_syllabus/{}/02/data/{}_{}.html"
        syllabus_res = requests.get(syllabus_url.format(nendo,nendo,td_tags[7].text.strip()))

        syllabus_soup = BeautifulSoup(syllabus_res.text, "html.parser")
        class_names = syllabus_soup.select('body > table:nth-of-type(2) > tr:nth-of-type(2) > td > table > tr:nth-of-type(3) > td:nth-of-type(2)')
        codes = syllabus_soup.select('body > table:nth-of-type(2) > tr:nth-of-type(2) > td > table >  tr:nth-of-type(2) > td:nth-of-type(2)')
        elems = syllabus_soup.select('.gaibu-syllabus')
        strip_syllabus = []
        important_list = []
        for name in class_names:
            important_list.append(name.text.strip())
        important_list.append(nendo)
        for code in codes:
            important_list.append(code.text.strip())

        for elem in elems:
            strip_syllabus.append(elem.text.strip())

        important_list.append(strip_syllabus[0]) #授業のテーマ
        # important_list.append(strip_syllabus[3])
        # important_list.append(strip_syllabus[4])
        sum_class_info.append(important_list)
        print(important_list)





        time.sleep(3)
        i+=1


        print(i)

driver = webdriver.Chrome()




#最初の画面
url = 'https://kym-syllabus.ofc.kobe-u.ac.jp/campussy/campussquare.do?_flowExecutionKey=_c35C8A384-F668-2E5A-45B6-70E95EEE7501_k0AE26F4C-E58E-D295-B242-496080162875'
driver.get(url)
time.sleep(1)

#国際文化学部を選択
element = driver.find_element_by_css_selector("#menu > li:nth-child(1)")
element.click()

#移動
element = driver.find_element_by_css_selector("#menu > li.sub.click > ul > li:nth-child(2) > a")
element.click()
time.sleep(1)

sum_class_info = []


#年度(2016年)を選択
nendo = 2016
element = driver.find_element_by_css_selector("#nendo")
indexNum = 5
select = Select(element)
#セレクトタグのオプションをインデックス番号から選択する
select.select_by_index(indexNum)
time.sleep(1)


#月曜日
page_source=driver.page_source
add_sum_class(nendo)

driver.quit()
