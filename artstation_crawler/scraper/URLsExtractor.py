# External libraries
from bs4 import BeautifulSoup


class URLsExtractor:
    """Searches the web page for image URLs.
    Args:
        html (str): The which will be searched for image URLs.
    """

    def __init__(self, html):
        self.html_soup = BeautifulSoup(html, 'html.parser')
        

    def get_urls(self):
        """Get the image URLs on this page.

        Returns:
            Union[List[str], None]: The URL list if URLs were found, otherwise None.
        """

        try:
            return self._urls_from_search()
        except:
            return None # Did not load fast enough, just go on with the next one.


    ###################
    # Private methods #
    ###################

    def _urls_from_search(self):
        """Get the URLs.

        Raises:
            Exception: If no URL was found.

        Returns:
            List[str]: A list of URLs.
        """

        extracted_urls = []
        img_elements = self.html_soup.find_all('img', { 'class': 'd-block' })

        for img_element in img_elements:
            url = img_element['src'].encode('utf-8')
            extracted_urls.append(url)

        return extracted_urls
