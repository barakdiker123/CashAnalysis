from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import requests
from selenium import webdriver

def scraper_data_stock(url, driver):
    #page = urlopen(url)
    #html = page.read().decode("utf-8")
    driver.get(url)
    html3 = driver.execute_script("return document.documentElement.innerHTML")

    soup = BeautifulSoup(html3, "html.parser")
    stock_last_gate = soup.find_all(id='stockPageMainFrame')
    print(float(stock_last_gate[0].div.div.contents[5].table.tr.contents[3].table.tr.contents[3].string.replace(',', '')))


url_table = "https://www.calcalist.co.il/stocks/home/0,7340,L-3961-198--2,00.html"
driver = webdriver.Chrome()
driver.get(url_table)
html = driver.execute_script("return document.documentElement.innerHTML")
soup = BeautifulSoup(html, "html.parser")
big_table_index = soup.find_all(id='ReccTblContent')[0].table.tbody

new_stock_url = "https://www.calcalist.co.il" + quote(big_table_index.tr.td.div.div.a["href"])

scraper_data_stock(new_stock_url , driver)
