# External libraries
from bs4 import BeautifulSoup

class URLExtractor:
    """Testbeschreibung.
    
    Raises:
        NotImplementedError: [description]
        NotImplementedError: [description]
        NotImplementedError: [description]
        TypeError: [description]
    
    Returns:
        [type] -- [description]
    """

    SEACH_PAGE = 'search'
    USER_PAGE = 'user'
    PIC_PAGE = 'picture'
    
    def __init__(self, html, page_title = None, page_url = None):
        self.page_title = page_title # Used for type identification
        self.html_soup = BeautifulSoup(html, 'html.parser')


    def get_urls(self):
        raise NotImplementedError


    ###################
    # Private methods #
    ###################

    def _urls_from_search(self):
        extracted_urls = []
        parents = self.html_soup.find_all('li', { 'class': 'gallery-grid-item' })

        for parent in parents:
            child = parent.find('a', recursive = False)
            url = child['href'].encode('utf-8')
            extracted_urls.append(url)

        return extracted_urls


    def _urls_from_pic_site(self, html_soup):
        raise NotImplementedError


    def _urls_from_profile(self, html_soup):
        raise NotImplementedError


    def _detect_type(self):
        if True:
            return self.USER_PAGE
        elif True:
            return self.SEACH_PAGE
        elif False:
            return self.PIC_PAGE
        else:
            raise TypeError('Neither HTML for artsation\'s search, user, or picture page provided.')

