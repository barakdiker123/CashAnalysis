from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import requests


url_table = "https://www.calcalist.co.il/stocks/home/0,7340,L-3961-198--2,00.html"
html = requests.get(url_table).text
soup = BeautifulSoup(html, "html.parser")
big_table_index = soup.find_all(id='ReccTblContent')[0]
#big_table_index = soup.find_all(id='GeneralTableFinanceData')[0]

print(big_table_index)
#print(big_table_index.parent.contents)
