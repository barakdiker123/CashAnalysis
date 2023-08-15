

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
from selenium import webdriver


import requests

def scraper_data_telaviv35(url ,driver):
    #page = urlopen(url)
    #html = page.read().decode("utf-8")
    #html2 = requests.get(url).text
    #driver = webdriver.Chrome()
    driver.get(url)
    html3 = driver.execute_script("return document.documentElement.innerHTML")

    soup = BeautifulSoup(html3, "html.parser")
    tel_aviv_35_last_gate = soup.find_all(id='stockIndexStatusFrame')
    print(tel_aviv_35_last_gate[0].div.div.div.div.ul.li.contents[1].string)

def scraper_data_stock(url, driver):
    #page = urlopen(url)
    #html = page.read().decode("utf-8")
    driver.get(url)
    html3 = driver.execute_script("return document.documentElement.innerHTML")

    soup = BeautifulSoup(html3, "html.parser")
    stock_last_gate = soup.find_all(id='stockPageMainFrame')
    print(float(stock_last_gate[0].div.div.contents[5].table.tr.contents[3].table.tr.contents[3].string.replace(',', '')))


driver = webdriver.Chrome()

url_tel_aviv_35 = "https://www.calcalist.co.il/stocks/home/0,7340,L-3961-198,00.html" + quote("?quote=מדד%20ת%22א%2035")
url_electra = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-739037,00.html" + quote("?quote=אלקטרה")
url_elbit = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-1081124,00.html" + quote("?quote=אלביט%20מערכות")
url_aloni_hayz = "https://www.calcalist.co.il/stocks/home/0,7340,L-3959-390013,00.html" + quote("?quote=אלוני%20חץ")


scraper_data_telaviv35(url_tel_aviv_35, driver)
scraper_data_stock(url_electra,driver)
scraper_data_stock(url_elbit,driver)
scraper_data_stock(url_aloni_hayz,driver)
