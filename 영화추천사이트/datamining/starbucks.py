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
url = "https://www.starbucks.co.kr/menu/drink_list.do"

# 접속 시도
driver.get(url)
html = driver.page_source
source = BeautifulSoup(html, 'html.parser')

link = source.select('dd > ul > li > dl > dt > a')



for i in link :

    detail_url = 'https://www.starbucks.co.kr/menu/drink_view.do?product_cd=' + i['prod']

    driver.get(detail_url)
    html = driver.page_source
    source = BeautifulSoup(html, 'html.parser')



    sub_data = dict()

    img = source.select('div.product_big_pic > p > a > img')[0]['src']
    print(img)
    sub_data['img'] = img

    name = source.select('div.myAssignZone > h4')[0].text.strip()
    sub_data['name'] = name
    summary = source.select('div.myAssignZone > p')[0].text.strip()
    sub_data['summary'] = summary

    tall_size = source.select('div.selectTxt2')[0].text.strip()
    sub_data['tall_size'] = tall_size
    serving_size = source.select('li.kcal > dl > dd')[0].text.strip()
    sub_data['serving_size'] = serving_size
    saturated_fat = source.select('li.sat_FAT > dl > dd')[0].text.strip()
    sub_data['saturated_fat'] = saturated_fat
    protein = source.select('li.protein > dl > dd')[0].text.strip()
    sub_data['protein'] = protein
    sodium = source.select('li.sodium > dl > dd')[0].text.strip()
    sub_data['sodium'] = sodium 
    sugars = source.select('li.sugars > dl > dd')[0].text.strip()
    sub_data['sugars'] = sugars
    caffeine_last = source.select('li.caffeine.last > dl > dd')[0].text.strip()
    sub_data['caffeine_last'] = caffeine_last   
    
    data.append(sub_data)



# txt 파일로 변환하기
with open('starbucks.txt', 'w', -1, "utf-8") as f:
    json.dump(data, f, ensure_ascii=False)