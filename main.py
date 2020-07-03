import requests
from bs4 import BeautifulSoup


def get_definitions_from_web(word: str, url: str = "https://dictionary.cambridge.org/dictionary/english/") -> list:
    """
    Cambridge Dictionary Scrapper
    """
    page_html: str = requests.get(url + word).text
    soup = BeautifulSoup(page_html, "html.parser")  # type: bs4.BeautifulSoup
    definitions: list = []
    counter: int = 0
    # "def ddef_d db" I checked looking up source in web browser
    for i, j in enumerate(soup.find_all("div", class_="def ddef_d db"), 1):
        # it is set to 3 because if there were more def then flashcard would be too much
        if counter < 3:
            definition = f"{i}. {j.text}".encode(encoding="utf-8", errors="replace")
            definitions.append(definition)
            counter += 1
        else:
            break
    return definitions


def print_definitions(word: str) -> None:
    print(word,
          get_definitions_from_web(word),
          sep="\n")


def save_definitions_to_file(word: str) -> None:
    with open("list_of_words.txt", "a") as list_of_words:
        list_of_words.write(f'\n{word}\t\"{get_definitions_from_web(word)}\"')


def save_definitions_interface(word: str) -> None:
    if word == "0":
        return None
    question = "Would you like to save (Y/N)?"
    print("#" * len(question))
    save_decision = input(question)
    if save_decision == "Y":
        save_definitions_to_file(word)


if __name__ == "__main__":
    word: str = ""
    while word != "0":
        word: str = input("Search english word (press 0 to exit): ").lower()
        print_definitions(word)
        save_definitions_interface(word)
