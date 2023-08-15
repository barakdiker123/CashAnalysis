

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#print(soup.get_text())
#image1, image2 = soup.find_all("img")
#print(image1.name)
#print(image1["src"])
sp = soup.find_all("h2")
print(sp[0].string)
print(soup.prettify())
sp1 = soup.find_all("body")
print(soup.head.title)
print(soup.body.center.find_all("img")[0]["src"])
