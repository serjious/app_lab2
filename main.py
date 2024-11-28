import requests
import re
from bs4 import BeautifulSoup
url = 'https://slovarozhegova.ru/letter.php?charkod=192'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

tag_name = "strong"
redex = r"([А-Я].+)"

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error: ", response.status_code)
    exit(1)
soup = BeautifulSoup(response.text, features="html.parser")
matched = soup.find_all(tag_name)

tandem = []
for i in matched:
    matched = re.findall(redex, i.text)
    tandem.extend(matched)

print(tandem)
#redex = r'<a href="/([а-я].+)/">.+</a>'
#matched= re.findall(redex, link.text) 

