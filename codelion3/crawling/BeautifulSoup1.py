from bs4 import BeautifulSoup
import requests
from datetime import datetime

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "http://www.daum.net/" #url 변수
response = requests.get(url) # get() url 조회하는 함수
soup = BeautifulSoup(response.text, 'html.parser')  #(데이터,파싱방법) 의미 없는 데이터를 사용할 수 있게 가공함
rank = 1

results = soup.findAll('a','link_favorsch') # 해당태그를 전부 검색하는 함수

# open(파일, 모드) 
# 모드 r(read)읽기, w(write)덮어쓰기, a(append)추가

search_rank_file = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위"+result.get_text()+"\n")       #write는 스트링을 지원
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1