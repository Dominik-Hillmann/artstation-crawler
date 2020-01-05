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
# External libraries
from bs4 import BeautifulSoup
# Typing
from typing import Callable
import chardet
from pprint import pprint
from splinter import Browser

# Self-written
from classes import URLManager

PIC_URL = 'https://www.artstation.com/artwork/ybG0yx'

def main():
    browser = Browser()
    browser.visit(PIC_URL)
    print(browser.title)
    markup = browser.html.encode('utf-8')
    soup = BeautifulSoup(markup, 'html.parser')

    pic_urls = []
    pics = soup.find_all('img', { 'class': 'img' })

    for pic in pics:
        pic_urls.append(pic['src'].encode('utf-8'))

    print(pic_urls)

    for pic_url in pic_urls:
        browser.visit(pic_url)
        browser.screenshot(os.path.join('C:', 'Users'))

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

