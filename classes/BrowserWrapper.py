#Python libraries
import os
import time

# External imports
from splinter import Browser

class BrowserWrapper:

    search_url = r'https://www.artstation.com/search?q='
    seach_options = r'&sort_by=relevance'
    scroll_js_code = r'window.scrollTo(0, -document.body.scrollHeight);'


    def __init__(self, search_terms, download_dir):
        self.download_dir = download_dir

        self.browser = Browser()
        self.search_terms = '%20'.join(search_terms)
        self.browser.visit(self.search_url + self.search_terms + self.seach_options)

        self.search_window = self.browser.windows[0]
    

    def __del__(self):
        self.browser.quit()
    

    def scroll_down(self):
        self.search_window.is_current = True
        self.browser.execute_script(self.scroll_js_code)


    def screenshot(self, url):
        self._open_in_seperate_window(url)
        time.sleep(10)
        pic_window = self.browser.windows[1]
        pic_window.is_current = True
        self.browser.screenshot(os.path.join(self.download_dir, 'pic.png'))
        pic_window.close()

    
    def get_search_markup(self):
        time.sleep(10) # Site is dynamic, needs a while to build up.
        self.search_window.is_current = True
        markup = self.browser.html.encode('utf-8')

        return markup

    
    ###################
    # Private methods #
    ###################

    def _open_in_seperate_window(self, url):
        self.browser.execute_script('window.open("{}");'.format(url))
