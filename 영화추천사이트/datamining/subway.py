# https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
# https://m.blog.naver.com/kiddwannabe/221177292446

def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import json
import requests 

#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기

driver = webdriver.Chrome('C:/Users/wjddy/Downloads/chromedriver/chromedriver.exe')




data = []




## main_page 들어오기

# 접속할 url
url = "http://subway.co.kr/sandwichList"

# 접속 시도
driver.get(url)
html = driver.page_source
source = BeautifulSoup(html, 'html.parser')

link = source.select('dd > ul > li > dl > dt > a')


# 클래식 
for i in range(1,7) :

    detail_url = 'http://subway.co.kr/sandwichView?param=cl0' + str(i)

    driver.get(detail_url)
    html = driver.page_source
    source = BeautifulSoup(html, 'html.parser')
    sub_data = dict()

    img = source.select('div.menu_img > img')[0]['src']
    sub_data['img'] = img

    name = source.select('h2.name')[0]
    sub_data['name'] = name 

    summary = source.select('p.summary')[0]
    sub_data['summary'] = summary

    recipe = source.select('div.recipe > ul')

    recipe_ = dict{}
    for j in recipe:
        recipe_img = j.select('div.img > img')[0]['src']
        recipe_['img'] = recipe_img

        recipe_title = j.selct('p')[0]
        recipe_['recipe_title '] = recipe_title 

    sub_data['recipe'] = 

    



    data.append(sub_data)

# 프레쉬라이드 

# 프리미엄

# 아침메뉴


# txt 파일로 변환하기
with open('starbucks.txt', 'w', -1, "utf-8") as f:
    json.dump(data, f, ensure_ascii=False)