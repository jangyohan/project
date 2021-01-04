import nltk 
import urllib
from nltk import tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from krwordrank.word import KRWordRank
# from wordcloud import WordCloud
# from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import re
import json
import requests 

data = []



SERIES_URL = 'https://serieson.naver.com'

for index in range(1,750) :
    ## main_page 들어오기
    print(f'{index}페이지 해결중입나다')
    headpage = requests.get("https://serieson.naver.com/movie/categoryList.nhn?categoryCode=ALL&orderType=star_score&sortingType=&mobileYn=&drmFreeYn=&freeYn=&discountYn=&tagCode=&page={0}".format(index)) 
    # headwebpage = urllib.request.urlopen('http://serieson.naver.com/movie/categoryList.nhn?categoryCode=ALL&orderType=star_score&sortingType=&mobileYn=&drmFreeYn=&freeYn=&discountYn=&tagCode=&page={0}'.format(index))
    source = BeautifulSoup(headpage.content, 'html.parser')
    
    # if '구매' == price_type:
    sub_el = source.findAll('a', {f'class': 'NPI=a:content'} )

    point = 0
    ### 한페이지의 Url 얻음
    for i in range(1,len(sub_el)+1):
        
        print(f'{index}페이지에 {i}번째 해결중입나다')
        if len(source.findAll('p', {f'class': 'price2 v2'})) != 0 :
            price_type = list(source.findAll('p', {f'class': 'price2 v2'})[i].children)[1]
            if '구매' in price_type:
                DETAIL_URL = SERIES_URL + str(sub_el[i]['href'])
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
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                    
                    try :
                        director = list(source.find('dd').children)[1].get_text()
                        movie_data['director'] = director
                        err_cnt += 1
                    except IndexError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue

                    try:
                        story = source.find('p',{f'class': 'con_tx'}).get_text()
                        movie_data['director'] = story
                        err_cnt += 1
                    except IndexError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                        
                    
                    try :
                        post = list(list(source.find('div',{f'class': 'poster'}).children)[1].children)[0]['src']
                        movie_data['post'] = post
                        err_cnt += 1
                    except IndexError:
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        
                        print(index,point,'여기에요 아저씨')
                        continue
                    
                    
                    
                    try :
                        star_score = list(list(source.find('div',{f'class': 'sc_view'}).children)[1].children)[3].get_text()
                        movie_data['star_score'] = star_score
                        err_cnt += 1
                    except IndexError:
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        print(index,point,'여기에요 아저씨')
                        continue
                        
                        
                    try :
                        genre = list(list(list(list(source.findAll('dl',{'class':'info_spec'})[0].children)[3].children)[1].children)[1].children)[1].get_text()
                        movie_data['genre'] = genre
                        err_cnt += 1
                    except IndexError:
                        print(index,point,'여기에요 아저씨')

                        continue
                    except AttributeError:
                        print(index,point,'여기에요 아저씨')
                        continue

                    try :
                        running_time = list(list(list(source.findAll('dl',{'class':'info_spec'})[0].children)[3].children)[1].children)[5].get_text()
                        movie_data['runnig_time'] = running_time
                        err_cnt += 1
                    except IndexError:
                        print(index,point,'여기에요 아저씨')
                        continue
                    except AttributeError:
                        print(index,point,'여기에요 아저씨')
                        continue
                    
                    if err_cnt == 7 :
                        data.append(movie_data)

                point += 1
                    


# txt 파일로 변환하기
with open('data.txt', 'w', -1, "utf-8") as f:
  json.dump(data, f, ensure_ascii=False)


