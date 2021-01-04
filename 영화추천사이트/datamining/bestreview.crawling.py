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



url = "https://nid.naver.com/nidlogin.login"

driver.get(url)
login = {
    "id" : "asdfg0237",
    "pw" : "rkddbal478@"
}

# 아이디와 비밀번호를 입력합니다.
clipboard_input('//*[@id="id"]', login.get("id"))
clipboard_input('//*[@id="pw"]', login.get("pw"))

driver.find_element_by_xpath('//*[@id="log.login"]').click()


# 접속할 url
url = "https://movie.naver.com/movie/board/review/list.nhn?best=monthly"

# 접속 시도
driver.get(url)

data = dict()



SERIES_URL = 'https://serieson.naver.com'

for index in range(1,68) :
    ## main_page 들어오기
    print(f'{index}페이지 해결중입나다')
    url = "https://movie.naver.com/movie/board/review/list.nhn?best=monthly&page={0}".format(index)
    # headpage = requests.get("https://series.naver.com/novel/categoryProductList.nhn?categoryTypeCode=adult&page={0}".format(index)) 
    
    driver.get(url)
    html = driver.page_source
    source = BeautifulSoup(html, 'html.parser')
    
    link = source.select('td.movie > a')

    for i in link :

        detail_url = 'https://movie.naver.com/movie/board/review/list.nhn' + i['href']
  
        driver.get(detail_url)
        html = driver.page_source
        source = BeautifulSoup(html, 'html.parser')
        title = source.select('div.choice_movie_info > h5 > a')[0].text.strip()

        try :
            data[str(title)]["count"] += 1

        except KeyError:
            sub_data = dict()
            sub_data["count"] = 1

            director = source.select('table.info_area > tbody > tr > td')[1].
            text.strip()
            # director = source.select('table.info_area > tbody > tr > td > a')[3].text.strip()
            print(director,'@@@@@@@@@@@@@@@@@@')
            sub_data["director"] = director

            data[title] = sub_data
            


# txt 파일로 변환하기
with open('best_data.txt', 'w', -1, "utf-8") as f:
    json.dump(data, f, ensure_ascii=False)