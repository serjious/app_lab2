import requests
import re
from bs4 import BeautifulSoup

class HTTP_requests_parser:
    def __init__(self, tag: str):
        self.__tag = tag
        self.__urls = []
    
    def add_url(self, url: str):
        self.__urls.append(url)
    
    def get_list_of_words(self):
        words = []
        for url in self.__urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features="html.parser")
            for i in soup.find_all(self.__tag):
                words.append(i.text)
        return words 
          
def search_tandem_word(list_of_word: list) -> list:
    redex = r"\b([А-Я]{4,})\b"
    tandem = []
    for i in list_of_word:
        matched_list = re.findall(redex, i)
        if len(matched_list) > 0:
            word = matched_list[0]
            len_word = len(word)
            if len_word % 2 == 0 and len_word > 0:
                if word[0:len_word//2] == word[len_word//2:len_word]:
                    tandem.append(word)
    return tandem

def main():
    url = 'https://slovarozhegova.ru/letter.php?charkod=193'
    url1 = 'https://slovarozhegova.ru/letter.php?charkod=195'
    tag_name = "strong"
    a = ["БАБА", "КИСА"]
    site = HTTP_requests_parser(tag_name)
    site.add_url(url)
    site.add_url(url1)
    print(search_tandem_word(site.get_list_of_words()))

main()

