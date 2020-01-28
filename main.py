import requests
from bs4 import BeautifulSoup


# url_google = 'https://translate.google.com.ua/?hl=en&tab=wT1#view=home&op=translate&sl=en&tl=pl&text='
url_cambridge = 'https://dictionary.cambridge.org/dictionary/english/'
word = input('Podaj angielskie słowo: ').lower()
url_page = url_cambridge + word

page_html = requests.get(url_page).text
# page_decoded = page.content.decode('UTF-8')

soup = BeautifulSoup(page_html, 'html.parser')


counter = 0
for i, j in enumerate(soup.find_all("div", class_="def ddef_d db")):
    if counter < 3:
        print(f'{i+1}. {j.text}')
        counter += 1
    else:
        break
