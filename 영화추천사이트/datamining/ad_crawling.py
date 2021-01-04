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
url = "https://serieson.naver.com/movie/categoryList.nhn?categoryCode=ALL"

# 접속 시도
driver.get(url)

data = []



SERIES_URL = 'https://serieson.naver.com'

for index in range(1,188) :
    ## main_page 들어오기
    print(f'{index}페이지 해결중입나다')
    url = "https://serieson.naver.com/movie/adult/recentList.nhn?page={0}".format(index)
    # headpage = requests.get("https://series.naver.com/novel/categoryProductList.nhn?categoryTypeCode=adult&page={0}".format(index)) 
    
    driver.get(url)
    html = driver.page_source
    source = BeautifulSoup(html, 'html.parser')
    
    # if '구매' == price_type:
    
    sub_el = source.findAll('a', {f'class': 'NPI=a:content'} )
    

    point = 0
    detail_url = source.findAll('a',{'class': 'NPI=a:content'})
    ### 한페이지의 Url 얻음
    for i in range(len(sub_el)):
        
        # print(f'{index}페이지에 {i+1}번째 해결중입나다')
        # print(source.findAll('p', {f'class': 'price2 v2'}))
        # if len(source.findAll('p', {f'class': 'price2 v2'})[i-1]) != 0 :
        #     # price_type = list(source.findAll('p', {f'class': 'price2 v2'})[i].children)[1]
        #     # if '구매' in price_type:



        
        DETAIL_URL = SERIES_URL + str(detail_url[i-1]['href'])
        detail_page = requests.get(DETAIL_URL)
        source = BeautifulSoup(detail_page.content, 'html.parser', from_encoding='utf-8') 
        info = source.find('a',{f'class': 'lk_airinfo NPI=a:info'})
        if info != None :
            err_cnt = 0
            LAST_URL = str(info['href'])
            movie_data = dict()
            last_page = requests.get(LAST_URL)
            source = BeautifulSoup(last_page.content, 'html.parser', from_encoding='utf-8')
            
            try :
                title = list(source.find('h3',{f'class': 'h_movie'}).children)[1].get_text()
                movie_data['title'] = title
                err_cnt += 1
            except IndexError:
                
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                
                print(index,i,'여기에요 아저씨')
                continue
            
            try :
                director = list(source.find('dd').children)[1].get_text()
                movie_data['director'] = director
                err_cnt += 1
            except IndexError:
                
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                
                print(index,i,'여기에요 아저씨')
                continue

            try:
                story = source.find('p',{f'class': 'con_tx'}).get_text()
                movie_data['director'] = story
                err_cnt += 1
            except IndexError:
                
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                
                print(index,i,'여기에요 아저씨')
                continue
                
            
            try :
                post = list(list(source.find('div',{f'class': 'poster'}).children)[1].children)[0]['src']
                movie_data['post'] = post
                err_cnt += 1
            except IndexError:
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                
                print(index,i,'여기에요 아저씨')
                continue
            
            
            
            try :
                star_score = list(list(source.find('div',{f'class': 'sc_view'}).children)[1].children)[3].get_text()
                movie_data['star_score'] = star_score
                err_cnt += 1
            except IndexError:
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                print(index,i,'여기에요 아저씨')
                continue
                
                
            try :
                genre = list(list(list(list(source.findAll('dl',{'class':'info_spec'})[0].children)[3].children)[1].children)[1].children)[1].get_text()
                movie_data['genre'] = genre
                err_cnt += 1
            except IndexError:
                print(index,i,'여기에요 아저씨')

                continue
            except AttributeError:
                print(index,i,'여기에요 아저씨')
                continue

            try :
                running_time = list(list(list(source.findAll('dl',{'class':'info_spec'})[0].children)[3].children)[1].children)[5].get_text()
                movie_data['runnig_time'] = running_time
                err_cnt += 1
            except IndexError:
                print(index,i,'여기에요 아저씨')
                continue
            except AttributeError:
                print(index,i,'여기에요 아저씨')
                continue

            
            
            if err_cnt == 7 :
                data.append(movie_data)
                

        point += 1
                        


# txt 파일로 변환하기
with open('ad_data.txt', 'w', -1, "utf-8") as f:
    json.dump(data, f, ensure_ascii=False)