from bs4 import BeautifulSoup
import requests
from lxml import etree, html
import pandas as pd

url = 'https://www.imdb.com/what-to-watch/popular/?ref_=hm_watch_pop'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
movieName = soup.find_all('span', "title")
#dom = etree.HTML(str(soup))
#mov = (dom.xpath('//*[@id="__next"]/main/div[2]/section/section/section/div[2]/div/div[1]/div/div[2]/a/span'))
#tree = html.fromstring(page.content)
#mov = tree.xpath('//*[@id="__next"]/main/div[2]/section/section/section/div[2]/div/div[1]/div/div[2]/a')


for m in movieName:
    print(m)