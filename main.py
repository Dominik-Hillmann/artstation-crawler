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
from classes.URLsExtractor import URLsExtractor
from classes.BrowserWrapper import BrowserWrapper

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
    urls_manager = URLsManager(
        params['search_terms'], 
        params['n_pics_in_batch'], 
        params['number_pictures']
    )    
    browser = BrowserWrapper(params['search_terms'], params['target_directory'])

    # print(browser.test_element_screenshot())


    try:
        while not urls_manager.total_pic_number_collected():
            while not urls_manager.urls_exceed_batch_size():
                browser.load_more_imgs()
                markup = browser.get_search_markup()
                urls = URLsExtractor(markup).get_urls()
                urls_manager.urls_into_queue(urls)

            while urls_manager.urls_left():
                url = urls_manager.get_next_url()
                browser.screenshot(url)

    except KeyboardInterrupt:
        urls_manager.print_url_list_sizes()
        urls_manager.write_urls()

    finally:
        del browser


def test_element_screenshot():
    browser = BrowserWrapper


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