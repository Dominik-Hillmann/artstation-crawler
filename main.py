'''
Intented structure:
    - get parameters from config files, and command line including search terms
    - get URLs from the search page using the search terms
    - for every picture page that we got this way:
        - Search in profile for other pictures
        - Search among commentators for pictures with fitting tags
    - until the amount of pictures is covered or there are no unused URLs
'''
# Python libraries
import requests
import os
import time
from pprint import pprint

# External libraries
from bs4 import BeautifulSoup

# Typing
from typing import Callable
import chardet
from pprint import pprint
from splinter import Browser
from selenium.webdriver.common.keys import Keys

# Self-written
from classes.URLsManager import URLsManager
from classes.URLExtractor import URLExtractor

from utils.ParameterParser import ParameterParser

PIC_URL = 'https://www.artstation.com/artwork/EV0lD2'
SEARCH_URL = 'https://www.artstation.com/search?q=winter&sort_by=relevance'
PROFILE_URL = 'https://www.artstation.com/alexbeddows'


PIC_PATH = '/'.join(['C:', 'Users', 'Dominik USER', 'Repositories', 'artstation-crawler'])
# tag projects-list
    # tag ul, class gallery-grid
        # tag li, class gallery-grid-item
            # tag a, href ist gesuchter link


# Idee: spaeter Upload in neuem Repo, ohne Erwaehnung artstation
def main():
    params = ParameterParser().get_params()
    pprint(params)
    urls_manager = URLsManager(params['search_terms'])

    # try:
    #     pass
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     pass


def test_url_extraction():
    browser = Browser()
    browser.visit(PROFILE_URL)
    time.sleep(10)
    markup = browser.html.encode('utf-8')
    extractor = URLExtractor(markup, PROFILE_URL)
    pprint(extractor.get_urls())

    browser.quit()


def test_download():
    browser = Browser()
    browser.visit(PIC_URL)
    print(browser.title)
    markup = browser.html.encode('utf-8')
    soup = BeautifulSoup(markup, 'html.parser')

    pic_urls = []
    pics = soup.find_all('img', { 'class': 'img' })

    for pic in pics:
        pic_urls.append(pic['src'].encode('utf-8'))

    try:
        for i, pic_url in enumerate(pic_urls):
            browser.visit(pic_url)
            browser.screenshot(PIC_PATH + '/pic_{}.png'.format(i))
    except Exception as e:
        print('WARNING:', e)
    finally:
        browser.quit()


def parse_parameters():
    # returns, depth search tree, search terms
    pass


def get_search_page_links(start_page_url, stop_condition):
    """[summary]
    
    Arguments:
        start_page_url {[type]} -- [description]
        stop_condition {[type]} -- [description]
    """
    pass


def add_to_queue():
    pass





def print_stats():
    pass


if __name__ == '__main__':
    main()