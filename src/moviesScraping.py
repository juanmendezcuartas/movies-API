from bs4 import BeautifulSoup
import requests
import pandas as pd
#url = 'https://www.imdb.com/what-to-watch/popular/?ref_=hm_watch_pop'
url = 'https://www.imdb.com'
page = requests.get(url, timeout=10)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find("title").string)
print(soup.p.string)
