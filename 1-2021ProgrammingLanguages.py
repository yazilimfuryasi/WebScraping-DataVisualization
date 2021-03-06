## https://yazilimfuryasi.com/python-veri-cekme-ve-gorsellestirme/

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import matplotlib.pyplot as plt

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.jetbrains.com/lp/devecosystem-2021/")
time.sleep(1)
kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

content = soup.find_all("div", {"class":"rt-mosaic-wrapper"})

languages = []
oran = []
diller = {}
for i in content:
    languages.append((i.find("div", {"class":"rt-mosaic-title"})).text)
    oran.append(i.find("span", {"class":"rt-mosaic-value__1"}).text.replace("%", ""))
s = 0
for i in range(len(languages)):
    if int(oran[i]) <= 8:
        s += int(oran[i])
        continue
    diller[languages[i]] = oran[i]
diller[languages[-1]] = s

plt.figure()
plt.pie(list(diller.values()), labels=list(diller.keys()), autopct='%1.1f%%', pctdistance=0.9)
plt.title("2021 Programlama Dillerinin Kullanım Oranı")
plt.show()
