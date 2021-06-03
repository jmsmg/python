from bs4 import BeautifulSoup
import requests

url = "http://www.naver.com/"
response = requests.get(url)
BeautifulSoup(response.text, 'html.parser')

