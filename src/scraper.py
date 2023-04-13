from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, poet_names=None, url=None):
        self.poet_names = poet_names
        self.url = url
        
    
    def set_poets_name(self, url: str)-> list:
        if url == "https://ganjoor.net/":
            self.url = url
            html_text = requests.get(url).text
            html_soup = BeautifulSoup(html_text,"lxml")
            divs_list = html_soup.find_all("div", class_="caption")
            addresses = [str(div.find("a")) for div in divs_list]
            poet_names = [address.split('"')[1][1:] for address in addresses]
            poet_names = list(set(poet_names))
            
            self.poet_names = poet_names
        else:
            raise ValueError("This program is not defined for scraping the provided URL.")
            
    @staticmethod
    def check_url(url: str)-> bool:
        try:
            get = requests.get(url)
            # if the request succeeds 
            if get.status_code == 200:
                return True
            else:
                return False
        #Exception
        except:
            return False
    
    def extend_url(self, extention):
        return self.url + extention