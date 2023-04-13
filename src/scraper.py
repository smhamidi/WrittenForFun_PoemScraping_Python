from urllib.request import urlopen

class Scraper:
    def __init__(self,):
        pass
    
    @staticmethod
    def get_poets_name(url: str)-> list:
        if url == "http://epub.ganjoor.net/":
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            html_list = list(html.split("\n"))
            html_list = [href for href in html_list if ("i.ganjoor" in href)]
            links = []
            for line in html_list:
                splited_line = list(line.split('"'))
                links.append([link for link in splited_line if "http" in link][0])
            names = [name.split("/")[-1].split(".")[0].lower() for name in links]
            return names
                                
        