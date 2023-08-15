

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

url = "https://www.calcalist.co.il/stocks/home/0,7340,L-3961-198,00.html" + quote("?quote=מדד%20ת%22א%2035")
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

tel_aviv_35_getter = soup.find_all(id='stockIndexStatusFrame')
print(float(tel_aviv_35_getter[0].div.div.div.div.ul.li.contents[1].string.replace(',', '')))

tel_aviv_35_index = float(tel_aviv_35_getter[0].div.div.div.div.ul.li.contents[1].string.replace(',', ''))

del url
del page
del html
del soup
