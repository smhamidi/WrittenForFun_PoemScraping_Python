from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

all_links = []
with open("./data/final_list.txt","r") as f:
    for name in f.read().splitlines():
        all_links.append(name)

for link in all_links:
    html_text = requests.get(link).text
    html_soup = BeautifulSoup(html_text,"lxml")
    text_list = html_soup.find_all("div", class_=["m1","n"])
    with open("PersianPoemsDataSet.txt", "a+") as f:
        for text in text_list[:-1]:
            f.write(text.text.encode("utf_8").decode("utf_8"))
        f.write(text_list[-1].text.encode("utf_8").decode("utf_8"))