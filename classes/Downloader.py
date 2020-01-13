# NOTE: Scrolldown for more pictures in browser: how to implement?
# External libraries
from splinter import Browser
# Self-written
from PageTypes import PageTypes

class Downloader:
    """Extracts information from different types of pages."""
    
    def __init__(self, url, download_destination):
        self.url = url.get_url()
        self.type = url.get_type()
        self.download_destination = download_destination
        self.browser = Browser()

    
    def get_type(self):
        return self.type


    def get_pic(self):
        if not self.type == PageTypes.PIC_VIEW:
            raise TypeError('To extract a picture, the page must be the picture view.')
        
        try:
            self.browser.visit(self.url)
            self.browser.screenshot(self.download_destination + '/pic.png')
        except Exception as e:
            print('WARNING: ' + str(e))
        finally:
            self.browser.quit()


    def get_urls(self, html_soup):
        raise NotImplementedError


    def get_tags(self):
        # Alternatively get_metainfo
        raise NotImplementedError

