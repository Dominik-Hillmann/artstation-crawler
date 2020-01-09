# External libraries
from bs4 import BeautifulSoup
# Self-written
from PageTypes import PageTypes
from URLWrapper import URLWrapper

class URLExtractor:
    
    def __init__(self, html, url):
        self.html_soup = BeautifulSoup(html, 'html.parser')
        self.url = URLWrapper(url)


    def get_urls(self):
        page_type = self.url.get_type()

        if page_type == PageTypes.PIC_VIEW:
            return self._urls_from_pic_site()
        elif page_type == PageTypes.SEARCH:
            return self._urls_from_search()
        elif page_type == PageTypes.PROFILE:
            return self._urls_from_profile()
    

    def get_type(self):
        return self.url.get_type()

    
    def get_pic_title(self):
        raise NotImplementedError


    def get_pic_description(self):
        raise NotImplementedError

    
    def get_pic_tags(self):
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


    def _urls_from_pic_site(self):
        extracted_urls = []
        commenter_names = self.html_soup.find_all('a', {'class': 'commenter-name' })
        base_url = 'https://www.artstation.com'

        for commenter_name in commenter_names:
            profile_name = commenter_name['href'].encode('utf-8')
            url = base_url + profile_name
            extracted_urls.append(url)
        
        return extracted_urls
    

    def _urls_from_profile(self):
        extracted_urls = []
        images = self.html_soup.find_all('img', { 'class': 'image' })

        for image in images:
            url = image['src'].encode('utf-8')
            extracted_urls.append(url)

        return extracted_urls
