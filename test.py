from ast import alias
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os
import webbrowser

baseURL = 'https://dict.naver.com/search.nhn?dicQuery='   #네이버백과사전링크

while True :
    inputURL = input('검색할 단어 : ')
    if inputURL == '그만' : break
    mixURL = baseURL + urllib.parse.quote_plus(inputURL) #한글로 쓰면 아스키코드로 자동 변환
    webbrowser.open(mixURL)
    html = urllib.request.urlopen(mixURL).read() #url링크 가져와서 읽음
    soup = BeautifulSoup(html, 'html.parser')
    #soup1=soup.get_text()
    bsSoup = soup.find("dd",align="left")
    aa=bsSoup.text
    #print(aa.lstrip())
    #print(aa.get_text(" ", strip=True) )
    aa = aa.replace("\n"," ") #공백 제거
    print(aa.strip())

os.system('pause')