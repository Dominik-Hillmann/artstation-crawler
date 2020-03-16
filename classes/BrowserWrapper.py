# Python libraries
import os
import time
from random import choice as rand_choice
# External imports
from splinter import Browser
import stem.process
from stem import Signal
from stem.control import Controller
from selenium.common.exceptions import WebDriverException


class BrowserWrapper:

    search_url = 'https://www.artstation.com/search?q='
    seach_options = '&sort_by=date'
    scroll_js_code = 'window.scrollBy(0, 50000);'

    proxyIP = '127.0.0.1'
    proxyPort = 9150
    proxy_settings = {
        'network.proxy.type': 1,
        'network.proxy.ssl': proxyIP,
        'network.proxy.ssl_port': proxyPort,
        'network.proxy.socks': proxyIP,
        'network.proxy.socks_port': proxyPort,
        'network.proxy.socks_remote_dns': True,
        'network.proxy.ftp': proxyIP,
        'network.proxy.ftp_port': proxyPort
    }

    def __init__(self, search_terms, download_dir):
        self.download_dir = download_dir
        self.browser = Browser()
        self.search_terms = '%20'.join(search_terms)
        self.browser.visit(self.search_url + self.search_terms + self.seach_options)
        self.search_window = self.browser.windows[0]
    

    def __del__(self):
        self.browser.quit()
    

    def load_more_imgs(self):
        """Scrolls search window by 1000 pixels, loading new pictures in the process."""

        self.search_window.is_current = True
        self.browser.execute_script(self.scroll_js_code)


    def screenshot(self, url):
        """Downloads the picture using its URL.
        
        Arguments:
            url {str} -- The URL unique to the picture.
        """

        self._open_in_seperate_window(url)
        self._random_wait_time()
        pic_window = self.browser.windows[1]
        pic_window.is_current = True

        screenshot_element = self.browser.find_by_css('img').first
        screenshot_element.screenshot(os.path.join(self.download_dir, 'pic.png'))
        
        pic_window.close()

    
    def get_search_markup(self):
        """Current markup of the dynamically loading page.
        
        Returns
        -------
            str -- The HTML markup of the search page.
        """

        self._random_wait_time()
        self.search_window.is_current = True
        markup = self.browser.html.encode('utf-8')

        return markup

    
    ###################
    # Private methods #
    ###################

    def _random_wait_time(self):
        num_wait_secs = rand_choice(list(range(10, 26)))
        time.sleep(num_wait_secs)


    def _switch_ip(self):
        raise NotImplementedError


    def _open_in_seperate_window(self, url):
        """Opens a link in a seperate window.
        
        Arguments:
            url {str} -- The URL to be opened in a seperate window.
        """

        self.browser.execute_script('window.open("{}");'.format(url))
