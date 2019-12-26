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
    header = {
        'Host': 'www.artstation.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': 1,
        'Connection': 'keep-alive',
        'Cookie': '__cfduid=d06324c170df1bf0e7f53424c2af5cb9c1577215010; visitor-uuid=1181f858-0bfb-4f82-badd-8b52422f2431; PRIVATE-CSRF-TOKEN=ObRRew0EFHXHtXGcctdj62CuXeHOUaDaX5xXstW4tt4%3D; country_code=DE; continent_code=EU; _pk_testcookie.2.119b=1; _pk_id.2.119b=ccd824f3b7206272.1577215030.3.1577224989.1577224989.; __stripe_mid=6d85f0a9-74dd-45f3-9030-0880f50db8bc; _ArtStation_session=V2x1bWZ4T2ZsaVhGYm1RVHdERWhoMGRTaHh0NVRRZnVpUXdpeFNYZkRmQjRPdUc2NzBlZkRicTNuVXNDcEExd1o0UGFMejA0WW1VUE42UVdSQlZNRkc1aW1lU2J6YjQ2SXg3TTNJcEYrcjlseEkwVThPdk04eWxCNmNXRDUzYlVHSkdzSUI2Z3NIdEdjWktiTDI4dEtENlNKK1pyb09Ua0NsdWNJR3lYNjdXQjZkOGxSblUyclRUdDByb0ptdms0MDhZc0UwU3E2SU1HdWJHVXdKVnZOUT09LS1jUXdNczBWOHlZeUwvOG1JT2ZlaElBPT0%3D--482379c2cfe52d8a7d82e5f091d39b79ca836176; __stripe_sid=96e78c67-329a-4d6c-b603-68f8abcd78cf'
    }
    markup = requests.get('http://www.artstation.com/search?q=space ship&sort_by=likes', headers = header)
    print(type(markup.text))
    print(markup.status_code)
    soup = BeautifulSoup(markup.text, features = 'html.parser')

    print(soup.prettify())


def parse_parameters():
    pass


def parse_web_pages(start_page_url: str, stop_condition: Callable):
    pass


def print_stats():
    pass


if __name__ == '__main__':
    main()
