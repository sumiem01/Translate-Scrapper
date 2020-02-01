import typing as t
import requests
from bs4 import BeautifulSoup


def get_definition(word: str, url: str = 'https://dictionary.cambridge.org/dictionary/english/') -> str:
    """
    Cambridge Dictionary Scrapper
    """
    page_html: str = requests.get(url + word).text
    soup = BeautifulSoup(page_html, 'html.parser')  # type: bs4.BeautifulSoup

    counter: int = 0
    back: str = ''
    # "def ddef_d db" I checked looking up source in web browser
    for i, j in enumerate(soup.find_all("div", class_="def ddef_d db")):
        if counter < 3:
            back += f'{i+1}. {j.text}\n'
            counter += 1
        else:
            break
    return back


if __name__ == '__main__':
    # word: str = input('Podaj angielskie słowo: ').lower()
    words: t.List['str'] = ['appear', 'shoe', 'headphones']
    for word in words:
        print(word)
        print(get_definition(word))
