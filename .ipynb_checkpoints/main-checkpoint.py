import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tld(tld, start=0, stop=100):
    tld_list = []
    i = start

    while i <= stop:
        GOOGLE_URL = lambda x: f'https://www.google.com/search?q={x}&start={i}'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'}

        req = requests.get(GOOGLE_URL(f'site:{tld}'), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')

        search_div = soup.find("div", id="rso")

        for t in search_div.find_all("div", {"class": "g"}):
            tld_list.append(t.find("div").find("div").find("a")['href'])

        i += 10

    return tld_list

for link in scrape_tld('finance'):
    print(link)