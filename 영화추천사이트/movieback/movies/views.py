def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)


from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.db.models import Q
import nltk 
# nltk.download()
import urllib
from nltk import tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from PIL import Image
from wordcloud import WordCloud as W_Cloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import json
import requests 
import json
import requests
import os

from .models import MovieData
from .models import Movie
from .models import M_data
from .models import Best_Review

from .serializers import MovieListSerializer
from .serializers import MovieSerializer
from .serializers import M_dataSerializer
from .serializers import Best_ReviewSerializer

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import json
import requests 


@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = M_dataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(M_data, pk=movie_pk)
    serializer = M_dataSerializer(movie)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, movie_pk):
    movie = get_object_or_404(M_data, pk=movie_pk)
    movie.delete()
    return Response({'message':'성공적으로 삭제되었습니다'})

@api_view(['PUT'])
def update(request, movie_pk):
    movie = get_object_or_404(M_data, pk=movie_pk)
    serializer = M_dataSerializer(data=request.data, instance=movie)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message':'성공적으로 수정되었습니다'})


@api_view(['POST'])
def search(request, query):
    movies = Movie.objects.all()
    movies.delete()

    import os
    import sys
    import urllib.request
    client_id = "aC5IYpf7i1PoavfLfsvr"
    client_secret = "RZhM4bRyOe"
    encText = urllib.parse.quote(query)
    url = f'https://openapi.naver.com/v1/search/movie.json?query={encText}' # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        # print(type(result))
        # print(type(result.items))
        # print(type(response_body))
        # print(response_body)
        # print(result['items'][0])
        m = Movie.objects.all()
        serializer = MovieSerializer(m,many=True)
        key = 0
        for item in result['items']:
            key += 1
            # print(item)
            movie = Movie()
            movie.title = item.get('title')
            movie.link = item.get('link')
            movie.image = item.get('image')
            movie.subtitle = item.get('subtitle')
            movie.pubDate = item.get('pubDate')
            movie.director = item.get('director')
            movie.actor = item.get('actor')
            movie.userRating = item.get('userRating')
            movie.key_id = key
            movie.save()
        return Response(serializer.data)
 
    else:
        print("Error Code:" + rescode)


@api_view(['GET'])
def dump(request):
    data = open("data/final.json", 'r', encoding='utf-8')
    crawling = eval(list(data)[0])
    
    for insert in crawling:
        movie_c = M_data()
        movie_c.title = insert['title']
        movie_c.content = insert['director']
        movie_c.post = insert['post']
        movie_c.genre = insert['genre']
        movie_c.score = insert['star_score']
        movie_c.time = insert['runnig_time']
        movie_c.save()
    return Response(crawling[0])





@api_view(['GET'])
def info(request, key):
    ### 링크 처리

    a = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={key}'
    terminator = a.index('basic')
    default = a[:terminator]
  

    terminator = a.index('.nhn')
    movie_code = a[terminator:]
  

    ### 
    main_url = '{0}pointWriteFormList{1}&type=after'.format(default,movie_code)

    U_score = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=159070&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=lowest&page={0}'


    info = []
    for j in range(1,30):
        webpage = urllib.request.urlopen(main_url+'&page={}'.format(j))

        source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
        for i in range(10):
            review_list = source.findAll('span', {f'id': '_filtered_ment_{0}'.format(i)})
            info.append(review_list[0].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))



    lines_list = ''


    for i in info:
        a = i.replace('영화관',"").replace('영화는',"").replace('영화가',"").replace('영화를',"").replace('인터스텔라',"").replace('영화',"").replace('그냥',"").replace('평점',"").replace('진짜',"").replace('정말',"").replace('아무것도',"").replace('에',"").replace('현재까지',"").replace('현재',"").replace('그런',"").replace('사람이',"").replace('사람',"").replace('만들',"").replace('어서',"").replace('솔직히',"").replace('겠다',"").replace('라고',"").replace('차라리',"").replace('아주',"").replace('않다',"").replace('말도',"").replace('안되',"").replace('점수',"").replace('들이',"").replace('없이',"").replace('어느',"").replace('위한',"").replace('힘든',"").replace('얼마나',"").replace('그리고',"").replace('그래서',"").replace('그러나',"").replace('는',"").replace('지금',"").replace('에서',"").replace('너무',"").replace('것을',"").replace('이런',"").replace('였다',"").replace('계속',"").replace('이게',"").replace('어떻게',"").replace('이건',"").replace('뭐가',"").replace('정도',"").replace('비해',"").replace('애들',"").replace('무슨',"").replace('내내',"").replace('아님',"").replace('모르고',"").replace('없고',"").replace('대해',"").replace('다시',"").replace('내가',"").replace('보고',"").replace('없다',"").replace('있다',"").replace('입니다',"").replace('와우',"").replace('가장',"").replace('같습니다',"").replace('무조건',"").replace('많이',"").replace('근데',"").replace('다들',"").replace('높은',"").replace('중간',"").replace('이다',"").replace('들은',"").replace('사실',"").replace('했다',"").replace('하데',"").replace('모르',"").replace('하나',"").replace('내용이',"").replace('내용',"").replace('볼때',"").replace('마다',"").replace('한번',"").replace('인간',"").replace('자체가',"").replace('있을까',"").replace('때',"").replace('시간',"").replace('감히',"").replace('이걸',"").replace('봤을',"").replace('봐도',"").replace('처음',"").replace('보니',"").replace('제대로',"").replace('역시',"").replace('대한',"").replace('어떤',"").replace('마치',"").replace('하지',"").replace('말이',"").replace('자체',"").replace('말고',"").replace('그렇게',"").replace('또한',"").replace('최고의',"").replace('이렇게',"").replace('다른',"").replace('극장',"").replace('의미가',"").replace('도대체',"").replace('작은',"").replace('싶다',"").replace('만든',"").replace('봤데',"").replace('만드',"").replace('그저',"").replace('나서',"").replace('보면',"").replace('대단하고',"").replace('아니',"").replace('재밌게',"").replace('두번',"").replace('변하지',"").replace('이제서야',"").replace('아닐까',"").replace('깊이',"").replace('같다',"").replace('중에',"").replace('넘어',"").replace('이제',"").replace('놀랍고',"").replace('않았다',"").replace('본게',"").replace('하고',"").replace('대해',"").replace('봤다',"").replace('모든',"").replace('부분이',"").replace('부터',"").replace('제발',"").replace('모두',"").replace('느껴지',"").replace('였습니다',"").replace('제가',"").replace('을',"").replace('보다',"").replace('아닌',"").replace('말로',"").replace('이보다',"").replace('끝까지',"").replace('봤지만',"").replace('이해',"").replace('를',"").replace('이거',"").replace('주변에',"").replace('민국',"").replace('느끼게',"").replace('것이',"")
        b = a.replace('이야',"").replace('이작품이',"").replace('나도',"").replace('돌아갈',"").replace('이후',"").replace('휴',"").replace('아이구',"").replace('아이쿠',"").replace('아이고',"").replace('어',"").replace('나',"").replace('우리',"").replace('저희',"").replace('따라',"").replace('의해',"").replace('을',"").replace('를',"").replace('에',"").replace('의',"").replace('가',"").replace('으로',"").replace('로',"").replace('에게',"").replace('뿐이다',"").replace('의거하여',"").replace('근거하여',"").replace('입각하여',"").replace('기준으로',"").replace('예하면',"").replace('예를 들면',"").replace('예를 들자면',"").replace('저',"").replace('소인',"").replace('소생',"").replace('저희',"").replace('지말고',"").replace('하지마',"").replace('하지마라',"").replace('다른',"").replace('물론',"").replace('또한',"").replace('그리고',"").replace('비길수 없다',"").replace('해서는 안된다',"").replace('뿐만 아니라',"").replace('만이 아니다',"").replace('만은 아니다',"").replace('막론하고',"").replace('관계없이',"").replace('그치지 않다',"").replace('그러나',"").replace('그런데',"").replace('하지만',"").replace('든간에',"").replace('논하지 않다',"").replace('따지지 않다',"").replace('설사',"").replace('비록',"").replace('더라도',"").replace('아니면',"").replace('만 못하다',"").replace('하는 편이 낫다',"").replace('불문하고',"").replace('향하여',"").replace('향해서',"").replace('향하다',"").replace('쪽으로',"").replace('틈타',"").replace('이용하여',"").replace('타다',"").replace('오르다',"").replace('제외하고',"").replace('이 외에',"").replace('이 밖에',"").replace('하여야',"").replace('비로소',"").replace('한다면 몰라도',"").replace('외에도',"").replace('이곳',"").replace('여기',"").replace('부터',"").replace('기점으로',"").replace('따라서',"").replace('할 생각이다',"").replace('하려고하다',"").replace('이리하여',"").replace('그리하여',"").replace('그렇게 함으로써',"").replace('하지만',"").replace('일때',"").replace('할때',"").replace('앞에서',"").replace('중에서',"").replace('보는데서',"").replace('으로써',"").replace('로써',"").replace('까지',"").replace('해야한다',"").replace('일것이다',"").replace('반드시',"").replace('할줄알다',"").replace('할수있다',"").replace('할수있어',"").replace('임에 틀림없다',"").replace('한다면',"").replace('등',"").replace('등등',"").replace('제',"").replace('겨우',"").replace('단지',"").replace('다만',"").replace('할뿐',"").replace('딩동',"").replace('댕그',"").replace('대해서',"").replace('대하여',"").replace('대하면',"").replace('훨씬',"").replace('얼마나',"").replace('얼마만큼',"").replace('얼마큼',"").replace('남짓',"").replace('여',"").replace('얼마간',"").replace('약간',"").replace('다소',"").replace('좀',"").replace('조금',"").replace('다수',"").replace('몇',"").replace('얼마',"").replace('지만',"").replace('하물며',"").replace('또한',"").replace('그러나',"").replace('그렇지만',"").replace('하지만',"").replace('이외에도',"").replace('대해 말하자면',"").replace('뿐이다',"").replace('다음에',"").replace('반대로',"").replace('반대로 말하자면',"").replace('이와 반대로',"").replace('바꾸어서 말하면',"").replace('바꾸어서 한다면',"").replace('만약',"").replace('그렇지않으면',"").replace('까악',"").replace('툭',"").replace('딱',"").replace('삐걱거리다',"").replace('보드득',"").replace('비걱거리다',"").replace('꽈당',"").replace('응당',"").replace('해야한다',"").replace('에 가서',"").replace('각',"").replace('각각',"").replace('여러분',"").replace('각종',"").replace('각자',"").replace('제각기',"").replace('하도록하다',"").replace('와',"").replace('과',"").replace('그러므로',"").replace('그래서',"").replace('고로',"").replace('한 까닭에',"").replace('하기 때문에',"").replace('거니와',"").replace('이지만',"").replace('대하여',"").replace('관하여',"").replace('관한',"").replace('과연',"").replace('실로',"").replace('아니나다를가',"").replace('생각한대로',"").replace('진짜로',"").replace('한적이있다',"").replace('하곤하였다',"").replace('하',"").replace('하하',"").replace('허허',"").replace('아하',"").replace('거바',"").replace('와',"").replace('오',"").replace('왜',"").replace('어째서',"").replace('무엇때문에',"").replace('어찌',"").replace('하겠는가',"").replace('무슨',"").replace('어디',"").replace('어느곳',"").replace('더군다나',"").replace('하물며',"").replace('더욱이는',"").replace('어느때',"").replace('언제',"").replace('야',"").replace('이봐',"").replace('어이',"").replace('여보시오',"").replace('흐흐',"").replace('흥',"").replace('휴',"").replace('헉헉',"").replace('헐떡헐떡',"").replace('영차',"").replace('여차',"").replace('어기여차',"").replace('끙끙',"").replace('아야',"").replace('앗',"").replace('아야',"").replace('콸콸',"").replace('졸졸',"").replace('좍좍',"").replace('뚝뚝',"").replace('주룩주룩',"").replace('솨',"").replace('우르르',"").replace('그래도',"").replace('또',"").replace('그리고',"").replace('바꾸어말하면',"").replace('바꾸어말하자면',"").replace('혹은',"").replace('혹시',"").replace('답다',"").replace('및',"").replace('그에 따르는',"").replace('때가 되어',"").replace('즉',"").replace('지든지',"").replace('설령',"").replace('가령',"").replace('하더라도',"").replace('할지라도',"").replace('일지라도',"").replace('지든지',"").replace('몇',"").replace('거의',"").replace('하마터면',"").replace('인젠',"").replace('이젠',"").replace('된바에야',"").replace('된이상',"").replace('만큼',"").replace('어찌됏든',"").replace('그위에',"").replace('게다가',"").replace('점에서 보아',"").replace('비추어 보아',"").replace('고려하면',"").replace('하게될것이다',"").replace('일것이다',"").replace('비교적',"").replace('좀',"").replace('보다더',"").replace('비하면',"").replace('시키다',"").replace('하게하다',"").replace('할만하다',"").replace('의해서',"").replace('연이서',"").replace('이어서',"").replace('잇따라',"").replace('뒤따라',"").replace('뒤이어',"").replace('결국',"").replace('의지하여',"").replace('기대여',"").replace('통하여',"").replace('자마자',"").replace('더욱더',"").replace('불구하고',"").replace('얼마든지',"").replace('마음대로',"").replace('주저하지 않고',"").replace('곧',"").replace('즉시',"").replace('바로',"").replace('당장',"").replace('하자마자',"").replace('밖에 안된다',"").replace('하면된다',"").replace('그래',"").replace('그렇지',"").replace('요컨대',"").replace('다시 말하자면',"").replace('바꿔 말하면',"").replace('즉',"").replace('구체적으로',"").replace('말하자면',"").replace('시작하여',"").replace('시초에',"").replace('이상',"").replace('허',"").replace('헉',"").replace('허걱',"").replace('바와같이',"").replace('해도좋다',"").replace('해도된다',"").replace('게다가',"").replace('더구나',"").replace('하물며',"").replace('와르르',"").replace('팍',"").replace('퍽',"").replace('펄렁',"").replace('동안',"").replace('이래',"").replace('하고있었다',"").replace('이었다',"").replace('에서',"").replace('로부터',"").replace('까지',"").replace('예하면',"").replace('했어요',"").replace('해요',"").replace('함께',"").replace('같이',"").replace('더불어',"").replace('마저',"").replace('마저도',"").replace('양자',"").replace('모두',"").replace('습니다',"").replace('가까스로',"").replace('하려고하다',"").replace('즈음하여',"").replace('다른',"").replace('다른 방면으로',"").replace('해봐요',"").replace('습니까',"").replace('했어요',"").replace('말할것도 없고',"").replace('무릎쓰고',"").replace('개의치않고',"").replace('하는것만 못하다',"").replace('하는것이 낫다',"").replace('매',"").replace('매번',"").replace('들',"").replace('모',"").replace('어느것',"").replace('어느',"").replace('로써',"").replace('갖고말하자면',"").replace('어디',"").replace('어느쪽',"").replace('어느것',"").replace('어느해',"").replace('어느 년도',"").replace('라 해도',"").replace('언젠가',"").replace('어떤것',"").replace('어느것',"").replace('저기',"").replace('저쪽',"").replace('저것',"").replace('그때',"").replace('그럼',"").replace('그러면',"").replace('요만한걸',"").replace('그래',"").replace('그때',"").replace('저것만큼',"").replace('그저',"").replace('이르기까지',"").replace('할 줄 안다',"").replace('할 힘이 있다',"").replace('너',"").replace('너희',"").replace('당신',"").replace('어찌',"").replace('설마',"").replace('차라리',"").replace('할지언정',"").replace('할지라도',"").replace('할망정',"").replace('할지언정',"").replace('구토하다',"").replace('게우다',"").replace('토하다',"").replace('메쓰겁다',"").replace('옆사람',"").replace('퉤',"").replace('쳇',"").replace('의거하여',"").replace('근거하여',"").replace('의해',"").replace('따라',"").replace('힘입어',"").replace('그',"").replace('다음',"").replace('버금',"").replace('두번째로',"").replace('기타',"").replace('첫번째로',"").replace('나머지는',"").replace('그중에서',"").replace('견지에서',"").replace('형식으로 쓰여',"").replace('입장에서',"").replace('위해서',"").replace('단지',"").replace('의해되다',"").replace('하도록시키다',"").replace('뿐만아니라',"").replace('반대로',"").replace('전후',"").replace('전자',"").replace('앞의것',"").replace('잠시',"").replace('잠깐',"").replace('하면서',"").replace('그렇지만',"").replace('다음에',"").replace('그러한즉',"").replace('그런즉',"").replace('남들',"").replace('아무거나',"").replace('어찌하든지',"").replace('같다',"").replace('비슷하다',"").replace('예컨대',"").replace('이럴정도로',"").replace('어떻게',"").replace('만약',"").replace('만일',"").replace('위에서 서술한바와같이',"").replace('인 듯하다',"").replace('하지 않는다면',"").replace('만약에',"").replace('무엇',"").replace('무슨',"").replace('어느',"").replace('어떤',"").replace('아래윗',"").replace('조차',"").replace('한데',"").replace('그럼에도 불구하고',"").replace('여전히',"").replace('심지어',"").replace('까지도',"").replace('조차도',"").replace('하지 않도록',"").replace('않기 위하여',"").replace('때',"").replace('시각',"").replace('무렵',"").replace('시간',"").replace('동안',"").replace('어때',"").replace('어떠한',"").replace('하여금',"").replace('네',"").replace('예',"").replace('우선',"").replace('누구',"").replace('누가 알겠는가',"").replace('아무도',"").replace('줄은모른다',"").replace('줄은 몰랏다',"").replace('하는 김에',"").replace('겸사겸사',"").replace('하는바',"").replace('그런 까닭에',"").replace('한 이유는',"").replace('그러니',"").replace('그러니까',"").replace('때문에',"").replace('그',"").replace('너희',"").replace('그들',"").replace('너희들',"").replace('타인',"").replace('것',"").replace('것들',"").replace('너',"").replace('위하여',"").replace('공동으로',"").replace('동시에',"").replace('하기 위하여',"").replace('어찌하여',"").replace('무엇때문에',"").replace('붕붕',"").replace('윙윙',"").replace('나',"").replace('우리',"").replace('엉엉',"").replace('휘익',"").replace('윙윙',"").replace('오호',"").replace('아하',"").replace('어쨋든',"").replace('차라리',"").replace('하는 편이 낫다',"").replace('흐흐',"").replace('놀라다',"").replace('상대적으로 말하자면',"").replace('마치',"").replace('아니라면',"").replace('쉿',"").replace('그렇지 않으면',"").replace('그렇지 않다면',"").replace('안 그러면',"").replace('아니었다면',"").replace('하든지',"").replace('아니면',"").replace('이라면',"").replace('좋아',"").replace('알았어',"").replace('하는것도',"").replace('그만이다',"").replace('어쩔수 없다',"").replace('하나',"").replace('일',"").replace('일반적으로',"").replace('일단',"").replace('한켠으로는',"").replace('오자마자',"").replace('이렇게되면',"").replace('이와같다면',"").replace('전부',"").replace('한마디',"").replace('한항목',"").replace('근거로',"").replace('하기에',"").replace('아울러',"").replace('하지 않도록',"").replace('않기 위해서',"").replace('이르기까지',"").replace('이 되다',"").replace('로 인하여',"").replace('까닭으로',"").replace('이유만으로',"").replace('이로 인하여',"").replace('그래서',"").replace('이 때문에',"").replace('그러므로',"").replace('그런 까닭에',"").replace('알 수 있다',"").replace('결론을 낼 수 있다',"").replace('으로 인하여',"").replace('있다',"").replace('어떤것',"").replace('관계가 있다',"").replace('관련이 있다',"").replace('연관되다',"").replace('어떤것들',"").replace('에 대해',"").replace('이리하여',"").replace('그리하여',"").replace('여부',"").replace('하기보다는',"").replace('하느니',"").replace('하면 할수록',"").replace('운운',"").replace('이러이러하다',"").replace('하구나',"").replace('하도다',"").replace('다시말하면',"").replace('다음으로',"").replace('에 있다',"").replace('에 달려 있다',"").replace('우리',"").replace('우리들',"").replace('오히려',"").replace('하기는한데',"").replace('어떻게',"").replace('어떻해',"").replace('어찌됏어',"").replace('어때',"").replace('어째서',"").replace('본대로',"").replace('자',"").replace('이',"").replace('이쪽',"").replace('여기',"").replace('이것',"").replace('이번',"").replace('이렇게말하자면',"").replace('이런',"").replace('이러한',"").replace('이와 같은',"").replace('요만큼',"").replace('요만한 것',"").replace('얼마 안 되는 것',"").replace('이만큼',"").replace('이 정도의',"").replace('이렇게 많은 것',"").replace('이와 같다',"").replace('이때',"").replace('이렇구나',"").replace('것과 같이',"").replace('끼익',"").replace('삐걱',"").replace('따위',"").replace('와 같은 사람들',"").replace('부류의 사람들',"").replace('왜냐하면',"").replace('중의하나',"").replace('오직',"").replace('오로지',"").replace('에 한하다',"").replace('하기만 하면',"").replace('도착하다',"").replace('까지 미치다',"").replace('도달하다',"").replace('정도에이르다',"").replace('할 지경이다',"").replace('결과에 이르다',"").replace('관해서는',"").replace('여러분',"").replace('하고 있다',"").replace('한 후',"").replace('혼자',"").replace('자기',"").replace('자기집',"").replace('자신',"").replace('우에 종합한것과같이',"").replace('총적으로 보면',"").replace('총적으로 말하면',"").replace('총적으로',"").replace('대로 하다',"").replace('으로서',"").replace('참',"").replace('그만이다',"").replace('할 따름이다',"").replace('쿵',"").replace('탕탕',"").replace('쾅쾅',"").replace('둥둥',"").replace('봐',"").replace('봐라',"").replace('아이야',"").replace('아니',"").replace('와아',"").replace('응',"").replace('아이',"").replace('참나',"").replace('년',"").replace('월',"").replace('일',"").replace('령',"").replace('영',"").replace('일',"").replace('이',"").replace('삼',"").replace('사',"").replace('오',"").replace('육',"").replace('륙',"").replace('칠',"").replace('팔',"").replace('구',"").replace('이천육',"").replace('이천칠',"").replace('이천팔',"").replace('이천구',"").replace('하나',"").replace('둘',"").replace('셋',"").replace('넷',"").replace('다섯',"").replace('여섯',"").replace('일곱',"").replace('여덟',"").replace('아홉',"").replace('령',"").replace('만 못하다',"").replace('하기보다는',"").replace('영',"").replace('아',"")
        lines_list += b

    print('전처리끝남')
    wordcloud = W_Cloud()
    text = lines_list
    wordcloud = wordcloud.generate_from_text(text)
  
    
    DIR_Cloud = settings.BASE_DIR
    print('경로설정')
   
    Cloud_ROOT = os.path.join(DIR_Cloud,'movies','media')
    wordcloud = W_Cloud(font_path= Cloud_ROOT +'/font/NanumSquareRegular.ttf',background_color='white').generate(text)
    Cloud_input = os.path.join(DIR_Cloud,'media','image')
    wordcloud.to_file(Cloud_input + f'/{key}.jpg')
    im = Image.open(Cloud_input + f'/{key}.jpg') # 이미지 불러오기

    print('마지막')
    return Response('성공')

@api_view(['GET'])
def best(request):
    #클립보드에 input을 복사한 뒤
    #해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
    DIR_ = settings.BASE_DIR

    DRIVE_ROOT = os.path.join(DIR_,'movies','media','chromedriver')
    driver = webdriver.Chrome(DRIVE_ROOT + '/chromedriver.exe')


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

                director = source.select('table.info_area > tbody > tr > td > a')[0].text.strip()
                sub_data["director"] = director

                data[title] = sub_data


    DIR_ = settings.BASE_DIR

    DATA_ROOT = os.path.join(DIR_,'data')

    # txt 파일로 변환하기
    with open(DATA_ROOT + 'best_data.json', 'w', -1, "utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


@api_view(['GET'])
def allmovie(request,selected):
    if selected == '전체':
        movie_c = M_data.objects.all()
        serializer = M_dataSerializer(movie_c, many=True)
        return Response(serializer.data)
    elif selected == '공포/스릴러':
        movie_c = M_data.objects.filter(Q(genre__contains='공포')|Q(genre__contains='스릴러'))
        serializer = M_dataSerializer(movie_c, many=True)
        return Response(serializer.data)    
    elif selected == 'SF/판타지':
        movie_c = M_data.objects.filter(Q(genre__contains='SF')|Q(genre__contains='판타지'))
        serializer = M_dataSerializer(movie_c, many=True)
        return Response(serializer.data)        
    
    else :
        movie_c = M_data.objects.filter(genre__contains=selected)
        serializer = M_dataSerializer(movie_c, many=True)
        return Response(serializer.data)
        



@api_view(['GET'])
def recommend(request,count):
    ## 내림차순으로 받아옴
    best = Best_Review.objects.all().order_by('-count')
    length = len(best)
    
    #### 5개씩 뽑아오고
    fiterList = best[count*5:(count*5)+5]
    serializer = Best_ReviewSerializer(fiterList, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def dump2(request):
    # data = open("data/data.json", 'r', encoding='utf-8')
    for i in range(1, 100):
        response = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=553cb93cdec029ea430dc27ac8866612&curPage={i}&itemPerPage=100')
        jsonData = response.json()

        # for item in jsonData["movieListResult"]['movieList']:
        #     if item.get('directors'):
        #         print(item.get('directors')[0].get('peopleNm'))
        #     if item.get('companys'):
        #         print(item.get('companys')[0].get('companyNm'))
        for item in jsonData["movieListResult"]['movieList']:
            movie = MovieData()
            movie.movieCd = item.get('movieCd')
            movie.movieNm = item.get('movieNm')
            movie.movieNmEn = item.get('movieNmEn')
            movie.prdtYear = item.get('prdtYear')
            movie.openDt = item.get('openDt')
            movie.typeNm = item.get('typeNm')
            movie.prdtStatNm = item.get('prdtStatNm')
            movie.nationAlt = item.get('nationAlt')
            movie.genreAlt = item.get('genreAlt')
            movie.repNationNm = item.get('repNationNm')
            movie.repGenreNm = item.get('repGenreNm')
            if item.get('directors'):
                movie.directors = item.get('directors')[0].get('peopleNm')
            if item.get('companys'):    
                movie.companys = item.get('companys')[0].get('companyNm')
            movie.save()
    
    return Response(jsonData["movieListResult"]['movieList'])

#데이터 insert 용
@api_view(['GET'])
def dump3(request):
    DIR_ = settings.BASE_DIR
   
    DATA_ROOT = os.path.join(DIR_,'data')
    print(DATA_ROOT,'@@@@@@@@@@@@@@@@@@@@@@')
    data = open(DATA_ROOT + "/best_data.json", 'r', encoding='utf-8')
    crawling = eval(list(data)[0])
    #"82년생 김지영": {"count": 7, "director": "김도영"}
    for insert in crawling:
        best = Best_Review()
        best.title = insert
        best.director = crawling[insert]['director']   
        best.count = crawling[insert]['count'] 
        print('최종전')
        best.save()
        print('최종후')
    return Response((crawling))