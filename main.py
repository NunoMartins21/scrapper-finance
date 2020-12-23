import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlsplit

def scrape_tld(tld, date=None, start=0, stop=100):
    tld_list = []
    i = start
    date_q = f'&tbs={date}' if date is not None else ''

    while i <= stop:
        GOOGLE_URL = lambda x: f'https://www.google.com/search?q={x}&start={i}{date_q}'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'}

        req = requests.get(GOOGLE_URL(f'site:{tld}'), headers=headers)
        print(GOOGLE_URL(f'site:{tld}'))
        soup = BeautifulSoup(req.text, 'html.parser')

        try:
            search_div = soup.find("div", id="rso")

            for t in search_div.find_all("div", {"class": "g"}):
                tld_list.append(urlsplit(t.find("div").find("div").find("a")['href']).netloc)

            i += 10
        except AttributeError as err:
            break

    return tld_list

tb = pd.DataFrame({".finance": scrape_tld('finance', date='qdr:d')})