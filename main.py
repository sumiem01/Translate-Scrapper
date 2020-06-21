import typing as t
import requests
from bs4 import BeautifulSoup


def get_definitions_from_web(word: str, url: str = "https://dictionary.cambridge.org/dictionary/english/") -> str:
    """
    Cambridge Dictionary Scrapper
    """
    page_html: str = requests.get(url + word).text
    soup = BeautifulSoup(page_html, "html.parser")  # type: bs4.BeautifulSoup

    counter: int = 0
    back: str = ""
    # "def ddef_d db" I checked looking up source in web browser
    for i, j in enumerate(soup.find_all("div", class_="def ddef_d db")):
        if counter < 3:
            back += f"<div><br>{i+1}. {j.text}</div>\n"
            counter += 1
        else:
            break
    return back


def print_definitions(word: str) -> None:
    print(word,
          get_definitions_from_web(word).replace("<div><br>", "")
                                        .replace("</div>", ""),
          sep="\n")


def save_definitions_to_file(word: str) -> None:
    with open("list_of_words.txt", "a") as list_of_words:
        list_of_words.write(f'\n{word}\t\"{get_definitions_from_web(word)}\"')


def save_definition_interface(word: str) -> None:
    if word == "0":
        return None
    save_decision = input("Would you like to save (Y/N)?")
    if save_decision == "Y":
        save_definitions_to_file(word)


if __name__ == "__main__":
    word: str = ""
    while word != "0":
        word: str = input("Search english word (press 0 to exit): ").lower()
        print_definitions(word)
        save_definition_interface(word)
