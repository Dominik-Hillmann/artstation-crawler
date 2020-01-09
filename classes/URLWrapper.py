from PageTypes import PageTypes

class URLWrapper:
    def __init__(self, url):
        self.url = url
        self.type = self._detect_type(url)
    

    def get_type(self):
        return self.type


    ###################
    # Private methods #
    ###################

    @staticmethod
    def _detect_type(url):
        search_term = '/search?'
        pic_term = '/artwork/'        

        if search_term in url:
            return PageTypes.SEARCH
        elif pic_term in url:
            return PageTypes.PIC_VIEW
        else:
            return PageTypes.PROFILE
