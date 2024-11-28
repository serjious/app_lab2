import requests
import re
from bs4 import BeautifulSoup

class HTTP_requests_parser:
    def __init__(self, tag: str):
        self.__tag = tag
        self.__urls = []
    
    def add_url(self, url):
        if isinstance(url, str):
            self.__urls.append(url)
        elif isinstance(url, list):
            self.__urls.extend(url)
    
    def get_list_of_words(self):
        words = []
        for url in self.__urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features="html.parser")
            for i in soup.find_all(self.__tag):
                words.append(i.text)
        return words 
          

def search_tandem_word(list_of_word: list) -> list:
    redex = r"\b(\w{2,})\1\b"
    tandem = []
    for i in list_of_word:
        matched_list = re.findall(redex, i)
        if len(matched_list) > 0:
            word = matched_list[0]*2
            tandem.append(word)
    return tandem

def get_list_from_file(path: str) -> list:
    fd = open(path, "r", encoding="utf8")
    return fd.read().split()
    close(fd)

def file():
    words = get_list_from_file("tandem.txt")
    print(search_tandem_word(words))

def main():
    url_raw = 'https://slovarozhegova.ru/letter.php?charkod='
    urls = []
    for url_id in range(192, 223+1):
        urls.append(f"{url_raw}{url_id}")
    tag_name = "strong"
    site = HTTP_requests_parser(tag_name)
    site.add_url(urls)
    print(search_tandem_word(site.get_list_of_words()))

if __name__ == "__main__":
    main()
    file()
