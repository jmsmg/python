import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)

# print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')

file = open("daum.html", "w")
file.write(response.text)
file.close()

print(soup.title)
print(soup.title.string)
print(soup.span) #span을 하나만 불러옴
print(soup.findAll('span')) ## 모든 span을 찾음

result = soup.findAll("a","link_favorsch")