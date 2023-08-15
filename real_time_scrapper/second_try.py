

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

def scraper_data_telaviv35(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    tel_aviv_35_last_gate = soup.find_all(id='stockIndexStatusFrame')
    print(tel_aviv_35_last_gate[0].div.div.div.div.ul.li.contents[1].string)

def scraper_data_stock(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stock_last_gate = soup.find_all(id='stockPageMainFrame')
    print(stock_last_gate[0].div.div.contents[5].table.tr.contents[3].table.tr.contents[3].string)


url_tel_aviv_35 = "https://www.calcalist.co.il/stocks/home/0,7340,L-3961-198,00.html" + quote("?quote=מדד%20ת%22א%2035")
url_electra = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-739037,00.html" + quote("?quote=אלקטרה")
url_elbit = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-1081124,00.html" + quote("?quote=אלביט%20מערכות")
url_aloni_hayz = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-390013,00.html" + quote("?quote=אלוני%20חץ")


scraper_data_telaviv35(url_tel_aviv_35)
scraper_data_stock(url_electra)
scraper_data_stock(url_elbit)
scraper_data_stock(url_aloni_hayz)
