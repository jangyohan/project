import nltk 
# nltk.download()
import urllib
from nltk import tokenize
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from krwordrank.word import KRWordRank
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import re
import json
from PIL import Image
## 인터스텔라 
high_score = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=45290&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=highest&page={0}'
low_score ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=45290&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=lowest&page={0}'
high_empathy = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=45290&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={0}'
late = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=45290&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=newest&page={0}'


## 엄복동
U_score = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=159070&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=lowest&page={0}'


info = []
for j in range(1,70):
    webpage = urllib.request.urlopen(U_score .format(j))
    source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
    for i in range(10):
        review_list = source.findAll('span', {f'id': '_filtered_ment_{0}'.format(i)})
        info.append(review_list[0].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))



lines_list = ''




for i in info:
    a = i.replace('영화관',"").replace('영화는',"").replace('영화가',"").replace('영화를',"").replace('인터스텔라',"").replace('영화',"").replace('그냥',"").replace('평점',"").replace('진짜',"").replace('정말',"").replace('아무것도',"").replace('에',"").replace('현재까지',"").replace('현재',"").replace('그런',"").replace('사람이',"").replace('사람',"").replace('만들',"").replace('어서',"").replace('솔직히',"").replace('겠다',"").replace('라고',"").replace('차라리',"").replace('아주',"").replace('않다',"").replace('말도',"").replace('안되',"").replace('점수',"").replace('들이',"").replace('없이',"").replace('어느',"").replace('위한',"").replace('힘든',"").replace('얼마나',"")
    b = a.replace('그리고',"").replace('그래서',"").replace('그러나',"").replace('는',"").replace('지금',"").replace('에서',"").replace('너무',"").replace('것을',"").replace('이런',"").replace('였다',"").replace('계속',"").replace('이게',"").replace('어떻게',"").replace('이건',"").replace('뭐가',"").replace('정도',"").replace('비해',"").replace('애들',"").replace('무슨',"").replace('내내',"").replace('아님',"").replace('모르고',"").replace('없고',"")
    c = b.replace('대해',"").replace('다시',"").replace('내가',"").replace('보고',"").replace('없다',"").replace('있다',"").replace('입니다',"").replace('와우',"").replace('가장',"").replace('같습니다',"").replace('무조건',"").replace('많이',"").replace('근데',"").replace('다들',"").replace('높은',"").replace('중간',"").replace('이다',"").replace('들은',"").replace('사실',"").replace('했다',"").replace('하데',"").replace('모르',"").replace('하나',"").replace('내용이',"").replace('내용',"")
    d = c.replace('볼때',"").replace('마다',"").replace('한번',"").replace('인간',"").replace('자체가',"").replace('있을까',"").replace('때',"").replace('시간',"").replace('감히',"").replace('이걸',"").replace('봤을',"").replace('봐도',"").replace('처음',"").replace('보니',"").replace('제대로',"").replace('역시',"").replace('대한',"").replace('어떤',"").replace('마치',"").replace('하지',"").replace('말이',"").replace('자체',"").replace('말고',"").replace('그렇게',"").replace('또한',"")
    e = d.replace('최고의',"").replace('이렇게',"").replace('다른',"").replace('극장',"").replace('의미가',"").replace('도대체',"").replace('작은',"").replace('싶다',"").replace('만든',"").replace('봤데',"").replace('만드',"").replace('그저',"").replace('나서',"").replace('보면',"").replace('대단하고',"").replace('아니',"").replace('재밌게',"").replace('두번',"").replace('변하지',"").replace('이제서야',"").replace('아닐까',"").replace('깊이',"").replace('같다',"").replace('중에',"").replace('넘어',"").replace('이제',"").replace('놀랍고',"").replace('않았다',"").replace('본게',"")
    f = e.replace('하고',"").replace('대해',"").replace('봤다',"").replace('모든',"").replace('부분이',"").replace('부터',"").replace('제발',"").replace('모두',"").replace('느껴지',"").replace('였습니다',"").replace('제가',"").replace('을',"").replace('보다',"").replace('아닌',"").replace('말로',"").replace('이보다',"").replace('끝까지',"").replace('봤지만',"").replace('이해',"").replace('를',"").replace('이거',"").replace('주변에',"").replace('민국',"").replace('느끼게',"").replace('것이',"")
    lines_list += f

with open('test.txt', 'w', -1, "utf-8") as f:
    json.dump(lines_list, f, ensure_ascii=False)


wordcloud = WordCloud()
text = lines_list
wordcloud = wordcloud.generate_from_text(text)



wordcloud = WordCloud(font_path='C:/Users/wjddy/Downloads/NanumFontSetup_TTF_ALL/NanumSquareRoundR.ttf', background_color='white').generate(text)
plt.figure(figsize=(15,15)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거
plt.show() 
plt.savefig('test.png')

wordcloud.to_file('N.png')