from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

second_layer_list = []
with open("./data/second_layer_links.txt","r") as f:
    for name in f.read().splitlines():
        second_layer_list.append(name)

all_links = list()
for link in second_layer_list:
    html_text = requests.get(link).text
    html_soup = BeautifulSoup(html_text,"lxml")
    par_list = html_soup.find_all("p", class_="poem-excerpt")
    addresses = [str(div.find("a")) for div in par_list]
    prefixs = [address.split('"')[1].split("/")[-1] for address in addresses]
    for prefix in prefixs:
        all_links.append(link+"/"+prefix)

with open("final_list.txt", "a+") as f:
    for name in all_links[:-1]:
        f.write(f"{name}\n")
    f.write(all_links[-1])