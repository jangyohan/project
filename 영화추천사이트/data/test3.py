import requests
import sys
import json
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
# sys.stdout = open('data.txt', 'w')
data = []
for i in range(1, 500):
    response = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=553cb93cdec029ea430dc27ac8866612&curPage={i}&itemPerPage=100')
    data.append(response.json()['movieListResult']['movieList'])


# print(data)
with open('data.json', 'w', -1, "utf-8") as f:
  json.dump(data, f, ensure_ascii=False)

