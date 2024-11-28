import requests
import re
from bs4 import BeautifulSoup

class MyTypeError(TypeError):
    def __init__(self, var_name, var):
        super().__init__(f"incorrect type for {var_name}: {type(var)}")


class HTTPRequestsError(Exception):
    def __init__(self, requests_code: int, requests_message: str):
        super().__init__(f"{requests_code}: {requests_message}")
        
        
class HTTP_requests_parser:
    def __init__(self, tag: str):
        if not isinstance(tag, str):
            raise MyTypeError("tag", tag)
        self.__tag = tag
        self.__urls = []
    
    def add_url(self, url):
        if isinstance(url, str):
            self.__urls.append(url)
        elif isinstance(url, list):
            self.__urls.extend(url)
        else:
            raise MyTypeError("url", url)
    
    def get_list_of_words(self):
        words = []
        for url in self.__urls:
            response = requests.get(url)
            if response.status_code != 200:
                raise HTTPRequestsError(response.status_code,
                                        response.reason)
            soup = BeautifulSoup(response.text, features="html.parser")
            for i in soup.find_all(self.__tag):
                words.append(i.text)
        return words 
          

def search_tandem_word(list_of_word: list) -> list:
    if not isinstance(list_of_word, list):
        raise MyTypeError("list_of_word", list_of_word)
    redex = r"\b([А-Я]{2,})\1\b"
    tandem = []
    for i in list_of_word:
        matched_list = re.findall(redex, i)
        if len(matched_list) > 0:
            word = matched_list[0]*2
            tandem.append(word)
    return tandem if len(tandem) > 0 else None

def get_list_from_file(path: str) -> list:
    if not isinstance(path, str):
        raise MyTypeError("path", path)
    fd = open(path, "r", encoding="utf8")
    words = fd.read().split()
    fd.close()
    return words

def file_data():
    words = get_list_from_file("tandem.txt")
    print("FILE: ", search_tandem_word(words))

def url_data():
    url_raw = 'https://slovarozhegova.ru/letter.php?charkod='
    urls = []
    for url_id in range(192, 223+1):
        urls.append(f"{url_raw}{url_id}")
    tag_name = "strong"
    site = HTTP_requests_parser(tag_name)
    site.add_url(urls)
    print("URL: ", search_tandem_word(site.get_list_of_words()))

def main():
    try:
        file_data()
        url_data()
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
