"""[summary]
"""

# Python libraries
import requests
# External libraries
from bs4 import BeautifulSoup
# Typing
from typing import Callable

EXAMPLE_URL = 'https://www.artstation.com/artwork/ybG0yx'

def main() -> None:
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    markup = requests.get('http://www.artstation.com', headers = header)
    print(type(markup.text))
    print(markup.status_code)
    soup = BeautifulSoup(markup.text, features = 'html.parser')

    # print(soup.prettify())


def parse_parameters():
    pass


def parse_web_pages(start_page_url: str, stop_condition: Callable):
    pass


def print_stats():
    pass


if __name__ == '__main__':
    main()
