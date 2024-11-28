import requests
import re
from bs4 import BeautifulSoup
url = 'https://slovarozhegova.ru/letter.php?charkod=193'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

tag_name = "strong"
redex = r"\b([А-Я]{4,})\b"

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error: ", response.status_code)
    exit(1)
soup = BeautifulSoup(response.text, features="html.parser")
matched = soup.find_all(tag_name)

tandem = []
for i in matched:
    matched_list = re.findall(redex, i.text)
    if len(matched_list) > 0:
        word = matched_list[0]
        len_word = len(word)
        if len_word % 2 == 0 and len_word > 0:
            if word[0:len_word//2] == word[len_word//2:len_word]:
                tandem.append(word)

print(tandem)
#redex = r'<a href="/([а-я].+)/">.+</a>'
#matched= re.findall(redex, link.text) 

